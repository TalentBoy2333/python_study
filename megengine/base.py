import numpy as np
import megengine as mge # 我们习惯将 MegEngine 缩写为 mge
import megengine.functional as F # 我们习惯将 functional 缩写为 F

from megengine import tensor
from megengine import Tensor

# 1. 生成 Python List，然后转化为 MegEngine Tensor
py_list = range(5)
print(mge.tensor(py_list))

# 2. 生成 Numpy ndarray，然后转化为 MegEngine Tensor
np_ndarray = np.arange(5).astype("float32")
print(mge.tensor(np_ndarray))

# 3. 使用 functional 模块直接生成 MegEngine Tensor
mge_tensor = F.arange(5)
print(mge_tensor)

print(mge_tensor.dtype)
print(type(mge_tensor))

new_tensor = mge_tensor.astype("float16")
print(new_tensor)

print(type(mge_tensor.numpy()))

print(tensor([1, 2, 3]))      # 实际上我们更希望使用 float32 类型的 Tensor
print(Tensor([1., 2., 3.]))   # 因此我们会习惯性地加上一个点表示这是浮点数

matrix_tensor = mge.tensor([[1., 2., 3.],
                            [4., 5., 6.]])
print(matrix_tensor.shape)

print(matrix_tensor.size)   # 2 * 3 = 6

''' 通过 item() 方法，我们可以获得对应的 Python 标量对象 '''
a = mge.tensor([[5.]])      # 可以多维，但必须确保其中只有一个元素，即 size 为 1
print(a.item(), type(a.item()))