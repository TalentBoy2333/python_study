import megengine as mge
import megengine.functional as F

''' 求导器（GradManager） '''
from megengine.autodiff import GradManager

w = mge.tensor([3.])
x = mge.tensor([2.])
b = mge.tensor(-1.)

gm = GradManager().attach([w, b])   # 新建一个求导器，绑定需要求导的变量，实例通常习惯写成 gm
with gm:                            # 开始记录计算图
    p = F.mul(w, x)
    y = p + b
    gm.backward(y)                  # 计算 y 关于参数的导数，过程中不断地使用链式法则

print(w.grad)                       # 得到结果为 x
print(b.grad)                       # 得到结果为 1

''' 优化器（Optimizer） '''
w = mge.Parameter([3.])
x = mge.Tensor([2.])
b = mge.Parameter(-1.)

print(type(w))
print(type(b))

gm = GradManager().attach([w, b])   # 这次 attach() 传入的是 Parameter 而不是 Tensor
with gm:
    p = F.mul(w, x)
    y = p + b
    gm.backward(y)

print(type(w.grad))                 # 计算得到的梯度依然是 Tensor

import megengine.optimizer as optim      # 我们习惯将 optimizer 缩写为 optim
import numpy as np 

optimizer = optim.SGD([w, b], lr=0.01)   # 实例化随机梯度下降（SGD）优化器，传入 Parameter w 和 b
optimizer.step()                         # 更新参数值 w = w - lr * w.grad
optimizer.clear_grad()                   # 将参数的梯度清空，节省内存，以便下一次计算，w.grad 变为 None

print(w, w.grad)

''' Loss '''
import megengine.functional as F

pred = np.array([3, 3, 3, 3]).astype(np.float32)
real = np.array([2, 8, 6, 1]).astype(np.float32)

loss = np.mean((pred - real) ** 2)       # 根据公式定义计算
print(loss)
loss = F.loss.square_loss(pred, real)    # MegEngine 中的实现
print(loss)