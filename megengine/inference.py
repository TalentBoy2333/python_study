import megengine as mge
import megengine.module as M
import megengine.functional as F
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
state_dict = mge.load("lenet.mge")
# 将参数加载到网络
le_net.load_state_dict(state_dict)

import megengine as mge
from megengine.data import DataLoader
from megengine.data.transform import ToMode, Pad, Normalize, Compose
from megengine.data import RandomSampler
from megengine.data.dataset import MNIST

# 读取测试数据并进行预处理
mnist_test_dataset = MNIST(root="./dataset/MNIST", train=False, download=True)
dataloader_test = DataLoader(
    mnist_test_dataset,
    transform=Compose([
        Normalize(mean=0.1307*255, std=0.3081*255),
        Pad(2),
        ToMode('CHW'),
    ]),
)

le_net.eval() # 设置为测试模式
# data = mge.tensor()
correct = 0
total = 0
for idx, (batch_data, batch_label) in enumerate(dataloader_test):
    data = mge.tensor(batch_data)
    logits = le_net(data)
    predicted = logits.numpy().argmax(axis=1)
    correct += (predicted==batch_label).sum()
    total += batch_label.shape[0]
print("correct: {}, total: {}, accuracy: {}".format(correct, total, float(correct)/total))


''' eval() 和 train() '''
import megengine as mge
from megengine.module import Dropout

dropout = Dropout(drop_prob=0.2) # 创建一个Dropout实例，每个值有0.2的概率置零
data = mge.tensor(np.random.randn(10).astype('float32')) # 原始数据
print("origin:", data)

dropout.train() # 训练时
print("\ntrain:", dropout(data))

dropout.eval() # 测试时
print("\neval:", dropout(data))
