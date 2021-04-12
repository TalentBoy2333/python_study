import megengine as mge
import megengine.module as M
import numpy as np

class LeNet(M.Module):
    def __init__(self):
        super(LeNet, self).__init__()
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
        # F.flatten 将原本形状为 (N, C, H, W) 的张量x从第一个维度（即C）开始拉平成一个维度，
        # 得到的新张量形状为 (N, C*H*W) 。 等价于 reshape 操作： x = x.reshape(x.shape[0], -1)
        x = F.flatten(x, 1)
        x = self.relu3(self.fc1(x))
        x = self.relu4(self.fc2(x))
        x = self.classifier(x)
        return x

# 实例化
le_net = LeNet()

from megengine.data import DataLoader
from megengine.data.transform import ToMode, Pad, Normalize, Compose
from megengine.data import RandomSampler
from megengine.data.dataset import MNIST

# 读取训练数据并进行预处理
mnist_train_dataset = MNIST(root="./dataset/MNIST", train=True, download=True)
dataloader = DataLoader(
    mnist_train_dataset,
    transform=Compose([
        Normalize(mean=0.1307*255, std=0.3081*255),
        Pad(2),
        ToMode('CHW'),
    ]),
    sampler=RandomSampler(dataset=mnist_train_dataset, batch_size=64, drop_last=True), # 训练时一般使用RandomSampler来打乱数据顺序
)

import megengine as mge
import megengine.functional as F
import megengine.optimizer as optim
import megengine.distributed as dist
from megengine.autodiff.grad_manager import GradManager

optimizer = optim.SGD(
    le_net.parameters(), # 参数列表，将指定参数与优化器绑定
    lr=0.05,  # 学习速率
)

gm = GradManager().attach(le_net.parameters()) # 定义一个求导器，将指定参数与求导器绑定

total_epochs = 10
for epoch in range(total_epochs):
    total_loss = 0
    for step, (batch_data, batch_label) in enumerate(dataloader):
        data = mge.tensor(batch_data)
        label = mge.tensor(batch_label, dtype="int32") # 交叉熵损失函数的标签数据需要是整型类型
        # data.set_value(batch_data)
        # label.set_value(batch_label)
        
        optimizer.clear_grad()      # 将参数的梯度置零
        with gm:                    # 记录计算图
            # logits为网络的输出结果，label是数据的真实标签即训练目标
            logits = le_net(batch_data)
            # 交叉熵损失函数
            loss = F.cross_entropy_with_softmax(logits, batch_label)
            gm.backward(loss)       # 反向传播计算梯度
        optimizer.step()            # 根据梯度更新参数值


        total_loss += loss.numpy().item()
    print("epoch: {}, loss {}".format(epoch, total_loss/len(dataloader)))

path = "lenet.mge"  # 我们约定用".mge"拓展名表示 MegEngine 模型文件
mge.save(le_net.state_dict(), path)



''' GPU和CPU切换 '''
'''
import megengine as mge

# 默认使用CPU
mge.set_default_device('cpux')
# 默认使用GPU
mge.set_default_device('gpux')

# 默认使用CPU
export MGE_DEFAULT_DEVICE='cpux'

# 默认使用GPU
export MGE_DEFAULT_DEVICE='gpux'
'''