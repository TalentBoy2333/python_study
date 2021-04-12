import numpy as np
from typing import Tuple

# 导入需要被继承的 Dataset 类
from megengine.data.dataset import Dataset

class XORDataset(Dataset):
    def __init__(self, num_points):
        """
        生成如图1所示的二分类数据集，数据集长度为 num_points
        """
        super().__init__()

        # 初始化一个维度为 (50000, 2) 的 NumPy 数组。
        # 数组的每一行是一个横坐标和纵坐标都落在 [-1, 1] 区间的一个数据点 (x, y)
        self.data = np.random.rand(num_points, 2).astype(np.float32) * 2 - 1
        # 为上述 NumPy 数组构建标签。每一行的 (x, y) 如果符合 x*y < 0，则对应标签为1，反之，标签为0
        self.label = np.zeros(num_points, dtype=np.int32)
        for i in range(num_points):
            self.label[i] = 1 if np.prod(self.data[i]) < 0 else 0

    # 定义获取数据集中每个样本的方法
    def __getitem__(self, index: int) -> Tuple:
        return self.data[index], self.label[index]

    # 定义返回数据集长度的方法
    def __len__(self) -> int:
        return len(self.data)

np.random.seed(2020)
# 构建一个包含 30000 个点的训练数据集
xor_train_dataset = XORDataset(30000)
print("The length of train dataset is: {}".format(len(xor_train_dataset)))

# 通过 for 遍历数据集中的每一个样本
for cor, tag in xor_train_dataset:
    print("The first data point is: {}, {}".format(cor, tag))
    break

print("The second data point is: {}".format(xor_train_dataset[1]))



''' 通过 Sampler 从 Dataset 中采样 '''
# 导入 MegEngine 中采样器
from megengine.data import RandomSampler

xor_dataset = XORDataset(30000)
# 创建一个随机采样器
random_sampler = RandomSampler(dataset=xor_dataset, batch_size=4)

# 获取迭代sampler时每次返回的数据集索引
for indices in random_sampler:
    print(indices)
    break


from megengine.data import SequentialSampler

sequential_sampler = SequentialSampler(dataset=xor_dataset, batch_size=4)

# 获取迭代sampler时返回的数据集索引信息
for indices in sequential_sampler:
    print(indices)
    break



''' 用 DataLoader 生成批数据 '''
from megengine.data import DataLoader

# 创建一个 DataLoader，并指定数据集和顺序采样器
xor_dataloader = DataLoader(
    dataset=xor_dataset,
    sampler=sequential_sampler,
)
print("The length of the xor_dataloader is: {}".format(len(xor_dataloader)))
# 从 DataLoader 中迭代地获取每批数据
for idx, (cor, tag) in enumerate(xor_dataloader):
    print("iter %d : " % (idx), cor, tag)
    break


''' MNIST dataset ''' 
# 从 MegEngine 中导入 MNIST 数据集
from megengine.data.dataset import MNIST

# 若你是第一次下载 MNIST 数据集，download 需设置成 True
# 若你已经下载 MNIST 数据集，通过 root 指定 MNIST数据集 raw 路径
# 通过 设置 train=True/False 获取训练集或测试集
mnist_train_dataset = MNIST(root="./dataset/MNIST", train=True, download=False)
# mnist_test_dataset = MNIST(root="./dataset/MNIST", train=False, download=True)
sequential_sampler = SequentialSampler(dataset=mnist_train_dataset, batch_size=4)

mnist_train_dataloader = DataLoader(
    dataset=mnist_train_dataset,
    sampler=sequential_sampler,
)

for i, batch_sample in enumerate(mnist_train_dataloader):
    batch_image, batch_label = batch_sample[0], batch_sample[1]
    # 下面可以将 batch_image, batch_label 传递给网络做训练，这里省略
    # trainging code ...
    # 中断
    break

print("The shape of minibatch is: {}".format(batch_image.shape))

# 导入可视化 Python 库，若没有请安装
import matplotlib.pyplot as plt

def show(batch_image, batch_label):
    for i in range(4):
        plt.subplot(1, 4, i+1)
        plt.imshow(batch_image[i][:,:,-1], cmap='gray')
        plt.xticks([])
        plt.yticks([])
        plt.title("label: {}".format(batch_label[i]))
    plt.show()

# 可视化数据
show(batch_image, batch_label)


''' Transform '''
# 导入 MegEngine 已支持的一些数据增强操作
from megengine.data.transform import RandomResizedCrop

dataloader = DataLoader(
    mnist_train_dataset,
    sampler=sequential_sampler,
    # 指定随机裁剪后的图片的输出size
    transform=RandomResizedCrop(output_size=28),
)

for i, batch_sample in enumerate(dataloader):
    batch_image, batch_label = batch_sample[0], batch_sample[1]
    break

show(batch_image, batch_label)


''' Compose Transform '''
from megengine.data.transform import RandomResizedCrop, Normalize, ToMode, Pad, Compose

# 利用 Compose 组合多个 Transform 操作
dataloader = DataLoader(
    mnist_train_dataset,
    sampler=sequential_sampler,
    transform=Compose([
        RandomResizedCrop(output_size=28),
        # mean 和 std 分别是 MNIST 数据的均值和标准差，图片数值范围是 0~255
        Normalize(mean=0.1307*255, std=0.3081*255),
        Pad(2),
        # 'CHW'表示把图片由 (height, width, channel) 格式转换成 (channel, height, width) 格式
        ToMode('CHW'),
    ])
)

for i, batch_sample in enumerate(dataloader):
    batch_image, batch_label = batch_sample[0], batch_sample[1]
    break

print("The shape of the batch is now: {}".format(batch_image.shape))