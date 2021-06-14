from megengine.data.dataset import MNIST

from megengine.data import DataLoader
from megengine.data.transform import ToMode, Pad, Normalize, Compose
from megengine.data.sampler import RandomSampler, SequentialSampler

# 如果使用 MegStudio 环境，请将 MNIST_DATA_PATH 为 /home/megstudio/dataset/MNIST/
MNIST_DATA_PATH = "./datasets/MNIST/"

# 获取训练数据集，如果本地没有数据集，请将 download 参数设置为 True
train_dataset = MNIST(root=MNIST_DATA_PATH, train=True, download=False)
test_dataset = MNIST(root=MNIST_DATA_PATH, train=False, download=False)

batch_size=64
# 创建 Sampler
train_sampler = RandomSampler(train_dataset, batch_size=batch_size)
test_sampler = SequentialSampler(test_dataset, batch_size=batch_size)

# 数据预处理方式
transform = Compose([
    Normalize(mean=0.1307*255, std=0.3081*255),
    Pad(2),
    ToMode('CHW'),
])

# 创建 Dataloader
train_dataloader = DataLoader(train_dataset, train_sampler, transform)
test_dataloader  = DataLoader(test_dataset, test_sampler, transform)

for X, y in train_dataloader:
    print("Shape of X: ", X.shape) # [N, C, H, W]
    print("Shape of y: ", y.shape, y.dtype)
    break