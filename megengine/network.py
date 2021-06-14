import megengine.module as M
import megengine.functional as F

# 定义网络，以经典的 LeNet 结构为例（但激活函数选用 ReLU）
class LeNet(M.Module):
    def __init__(self):
        super().__init__()
        # 单信道图片, 两层  5x5 卷积 + ReLU + 池化
        self.conv1 = M.Conv2d(1, 6, 5)
        self.relu1 = M.ReLU()
        self.pool1 = M.MaxPool2d(2, 2)
        self.conv2 = M.Conv2d(6, 16, 5)
        self.relu2 = M.ReLU()
        self.pool2 = M.MaxPool2d(2, 2)
        # 两层全连接 + ReLU
        self.fc1 = M.Linear(16 * 5 * 5, 120)
        self.relu3 = M.ReLU()
        self.fc2 = M.Linear(120, 84)
        self.relu4 = M.ReLU()
        # 分类器
        self.classifier = M.Linear(84, 10)

    def forward(self, x):
        x = self.pool1(self.relu1(self.conv1(x)))
        x = self.pool2(self.relu2(self.conv2(x)))
        # F.flatten 将原本形状为 (N, C, H, W) 的张量 x 从第一个维度（即 C）开始拉平成一个维度，
        # 得到的新张量形状为 (N, C*H*W) 。 等价于 reshape 操作： x = x.reshape(x.shape[0], -1)
        x = F.flatten(x, 1)
        x = self.relu3(self.fc1(x))
        x = self.relu4(self.fc2(x))
        x = self.classifier(x)
        return x

# 实例化网络
net = LeNet()
print(net)