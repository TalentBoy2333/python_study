import numpy as np
import megengine as mge

# 初始化一个维度为 (2, 5) 的 ndarray，并转化成 MegEngine 的 Tensor
# 注：目前 MegEngine Tensor 不支持 float64 数值类型，所以这里我们显式指定了 ndarray 的数值类型
print('Tensor定义')
a = mge.tensor(np.random.random((2,5)).astype('float32'))
print(a)

# 初始化一个长度为3的列表，并转化成 Tensor
b = mge.tensor([1., 2., 3.])
print(b)
print()

print('Tensor赋值')
c = mge.tensor([1., 2., 3.])
print(c)
c.set_value(np.random.random((2,5)).astype("float32"))
# 此时我们将 Tensor c 进行了赋值
print(c)
print(c.dtype)
d = c.astype("float16")
print(d.dtype)
print(c.shape)
print()

print('Tensor转numpy')
a = mge.tensor(np.random.random((2,5)).astype('float32'))
print(a)
b = a.numpy()
print(b)
print()

print('算子')
a = mge.tensor(np.random.random((2,5)).astype('float32'))
print(a)
b = mge.tensor(np.random.random((2,5)).astype('float32'))
print(b)
print(a + b)
print()

print('切片')
print(a[1, :])
print('reshape')
a = a.reshape(5, 2)
print(a)
a = a.reshape(1, -1)
print(a.shape)
print()

print('矩阵乘')
import megengine.functional as F

a = mge.tensor(np.random.random((2,3)).astype('float32'))
print(a)
b = mge.tensor(np.random.random((3,2)).astype('float32'))
print(b)
c = F.matmul(a, b)
print(c)
print()

print('设备')
print(a.device)
b = a.to("cpu0")
print(b.device)
print()

print('BP')
import megengine as mge
import megengine.functional as F
from megengine.autodiff import GradManager

x = mge.tensor([1., 3., 5.]).reshape(1, 3)
w = mge.tensor([2., 4., 6.]).reshape(3, 1)
b = mge.tensor(-1.)

gm = GradManager().attach([w, b])   # 新建一个求导器，绑定需要求导的变量
with gm:                            # 开始记录计算图
    p = F.matmul(x, w)
    y = p + b
    gm.backward(y)                  # 计算 y 的导数

print(w.grad)
print(b.grad)