import numpy as np 
import torch 

np_data = np.arange(6).reshape(2,3)
torch_data = torch.from_numpy(np_data)
tensor2array = torch_data.numpy()

print(
    'numpy data:\n', np_data, 
    'torch data:\n', torch_data, 
    'tensor2array:\n', tensor2array
)

data = [-1, -2, 1, 2]
tensor = torch.FloatTensor(data)  # 32bit

print(
    'numpy abs:', np.abs(data),
    'torch abs:', torch.abs(tensor)
)

data = [[1,2], [3,4]]
tensor = torch.FloatTensor(data)
print(
    'numpy mat mul:', np.matmul(data, data), 
    'torch mat mul:', torch.mm(tensor, tensor)
)