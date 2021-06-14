import numpy as np
import matplotlib.pyplot as plt
from megengine.data.dataset import MNIST

# 强烈推荐使用 MegStudio 平台，可在项目设置中直接选用 MNIST 数据集，无需再进行下载
# 如果使用 MegStudio 环境，请将 MNIST_DATA_PATH 为 /home/megstudio/dataset/MNIST/
MNIST_DATA_PATH = "./datasets/MNIST/"

# 国内网络环境从 MNIST 数据集官方主页下载数据集可能会有些慢，可人为下载好以下文件后，放置在 MNIST_DATA_PATH 对应的路径
#     t10k-images-idx3-ubyte.gz
#     t10k-labels-idx1-ubyte.gz
#     train-images-idx3-ubyte.gz
#     train-labels-idx1-ubyte.gz

# 获取训练数据集，如果本地没有数据集，请将 download 参数设置为 True
train_dataset = MNIST(root=MNIST_DATA_PATH, train=True, download=False)

print(train_dataset.meta)
print(len(train_dataset), type(train_dataset[0]))
print(len(train_dataset[0]), train_dataset[0][0].shape, train_dataset[0][1].shape)

train_data = np.array([t[0] for t in train_dataset])
train_label = np.array([t[1] for t in train_dataset])
print(train_data.shape, train_label.shape)

classes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
num_classes = len(classes)
samples_per_class = 7

# 注意：初学者在接触本小节的可视化代码时可不求甚解，只在意其展示效果并阅读后面的部分，学有余力者可尝试搞清楚代码细节。
# for y, cls in enumerate(classes):
#     idxs = np.squeeze(np.where(train_label == y))
#     idxs = np.random.choice(idxs, samples_per_class, replace=False)
#     for i, idx in enumerate(idxs):
#         plt_idx = i * num_classes + y + 1
#         plt.subplot(samples_per_class, num_classes, plt_idx)
#         plt.imshow(train_data[idx], cmap="gray")
#         plt.axis('off')
#         if i == 0:
#             plt.title(cls)
# plt.show()

from megengine import tensor
import megengine.functional as F

''' flatten '''
x = tensor(np.random.random((10, 28, 28, 1)))
out = F.flatten(x, start_axis=1, end_axis=-1)  # 将从 start_axis 维到 end_axis 维的子张量展平
print(x.shape)
print(out.shape)

''' Softmax '''
# 举例：某张手写数字图片的对应标签为 3，进行 one-hot 编码表示
inp = tensor([3])
out = F.one_hot(inp, num_classes=10)
print(out.numpy()) # 输出是 2-D 的，因为将数量 n 也包括进去了，此时 n=1

# 也可以选择将整个 train_label 转换成 one_hot 编码
print(F.one_hot(tensor(train_label), num_classes=10).shape)

inp = tensor([1., 2., 3., 4.])
average = F.div(inp, F.sum(inp))
softmax = F.softmax(inp)
print(average.numpy().round(decimals=4))
print(softmax.numpy().round(decimals=4))

''' 交叉熵（Cross Entropy） '''
# 预测值完全准确的情况，loss 应该为 0
pred = tensor([0., 0., 0., 1., 0.,
               0., 0., 0., 0., 0.]).reshape(1, -1)
label = tensor([3])
loss = F.loss.cross_entropy(pred, label, with_logits=False)
print(loss.item())

# 预测值比较准确的情况
pred = tensor([0., 0., 0.3, 0.7, 0.,
               0., 0., 0., 0., 0.]).reshape(1, -1)
label = tensor([3])
loss = F.loss.cross_entropy(pred, label, with_logits=False)
print(loss.item())

# 预测值不那么准确的情况
pred = tensor([0., 0., 0.7, 0.3, 0.,
               0., 0., 0., 0., 0.]).reshape(1, -1)
label = tensor([3])
# 设置 with_logits=True 时，将使用 Softmax 函数把分类输出标准化成概率分布，下面的代码示例中 pred 已经为概率分布的形式；
loss = F.loss.cross_entropy(pred, label, with_logits=False)
print(loss.item())

