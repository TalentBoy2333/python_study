import numpy as np
from sklearn.datasets import load_boston

# 获取 boston 房价数据集，需要安装有 scikit-learn 这个库
boston = load_boston()

# 查看 boston 对象内部的组成结构
print(boston.keys())

# 查看数据集描述，内容比较多，因此这里注释掉了
# print(boston.DESCR)

# 查看 data 和 target 信息，这里的 target 可以理解成 label
print(boston.data.shape, boston.target.shape)

X, y = boston.data, boston.target
num, dim = X.shape

print(X[0], y[0]) # 取出第一个样本，查看对应的特征向量和标签值

mask = 500  # 这个值是随意设计的，不用想太多背后的原因

train_dataset = X[:mask]
test_dataset = X[mask:num]
train_label = y[:mask]
test_label = y[mask:num]

print(len(train_dataset), len(train_label))
print(len(test_dataset), len(test_label))

from typing import Tuple
from megengine.data.dataset import Dataset

class BostonTrainDataset(Dataset):
    def __init__(self):
        self.data = train_dataset
        self.label = train_label

    def __getitem__(self, index: int) -> Tuple:
        return self.data[index], self.label[index]

    def __len__(self) -> int:
        return len(self.data)

boston_train_dataset = BostonTrainDataset()
print(len(boston_train_dataset))

from megengine.data import DataLoader
from megengine.data import SequentialSampler

sequential_sampler = SequentialSampler(dataset=boston_train_dataset, batch_size=100)
train_dataloader = DataLoader(dataset=boston_train_dataset, sampler=sequential_sampler)

for batch_data, batch_label in train_dataloader:
    print(batch_data.shape, batch_label.shape, len(train_dataloader))
    break
