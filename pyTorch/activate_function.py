import torch
from torch.autograd import Variable
import numpy as np 
import matplotlib.pyplot as plt 

x = torch.linspace(-5, 5, 200)
x = Variable(x)
x_np = x.data.numpy()

print('x:', x_np)

y_relu = torch.relu(x).data.numpy()
y_sigmoid = torch.sigmoid(x).data.numpy()
y_tanh = torch.tanh(x).data.numpy()

plt.figure(1, figsize=(8,6))
plt.subplot(131)
plt.plot(x_np, y_relu, c='red', label='relu')
plt.ylim(-1,5)
plt.legend(loc='best')

plt.subplot(132)
plt.plot(x_np, y_sigmoid, c='red', label='sigmoid')
plt.ylim(-0.2,1.2)
plt.legend(loc='best')

plt.subplot(133)
plt.plot(x_np, y_tanh, c='red', label='tanh')
plt.ylim(-1.2,1.2)
plt.legend(loc='best')

plt.show()

