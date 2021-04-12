''' 基于 functional 搭建网络 ''' 
import megengine as mge
import megengine.functional as F
import numpy as np

def two_layer_conv(x):
    # (8, 3, 3, 3) 代表（输出信道数，输入信道数，卷积核高度，卷积核宽度）
    conv_weight = mge.Parameter(np.random.randn(8, 3, 3, 3).astype(np.float32))
    # 对于 8 个卷积核，提供 8 个 bias
    conv_bias = mge.Parameter(np.zeros((1, 8, 1, 1), dtype=np.float32))
    x = F.conv2d(x, conv_weight, conv_bias)
    x = F.relu(x)
    conv_weight = mge.Parameter(np.random.randn(16, 8, 3, 3).astype(np.float32))
    conv_bias = mge.Parameter(np.zeros((1, 16, 1, 1), dtype=np.float32))
    x = F.conv2d(x, conv_weight, conv_bias)
    x = F.relu(x)
    return x

# 输入形状为 (2, 3, 32, 32) 的张量
x = mge.tensor(np.random.randn(2, 3, 32, 32).astype(np.float32))
out = two_layer_conv(x)
print(out.shape)  # 输出： (2, 16, 28, 28)

''' 基于 Module 搭建网络 ''' 
import megengine.module as M

# 为了演示，我们在这里定义了一个简单的卷积模块。注意： MegEngine 已经提供了更为通用的 Conv2d 模块。
class ConvReLU(M.Module):
    def __init__(self, in_channels, out_channels):
        # 先调用父类的初始化
        super().__init__()

        # Conv
        self.conv = M.Conv2d(
            in_channels=in_channels, 
            out_channels=out_channels, 
            kernel_size=3, stride=1, padding=1, dilation=1, groups=1, bias=True
            )
        # 将激活函数 ReLU 作为子模块
        self.relu = M.ReLU()

    def forward(self, x):
        x = self.conv(x)
        x = self.relu(x)
        return x


# 基于 ConvReLU ，定义一个两层卷积网络
class TwoLayerConv(M.Module):
    def __init__(self):
        super().__init__()
        self.conv_relu1 = ConvReLU(3, 8)
        self.conv_relu2 = ConvReLU(8, 16)

    def forward(self, x):
        x = self.conv_relu1(x)
        x = self.conv_relu2(x)
        return x

# 输入形状为 (2, 3, 32, 32) 的张量
x = mge.tensor(np.random.randn(2, 3, 32, 32).astype(np.float32))
two_layer_conv_module = TwoLayerConv()
out = two_layer_conv_module(x)
print(out.shape)  # 输出： (2, 16, 28, 28)

conv_relu = ConvReLU(2, 3)
print(conv_relu.state_dict())
print(conv_relu.state_dict()['conv.bias'].shape)
