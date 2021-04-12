import torch 
from torch.autograd import Variable
import numpy as np 


class CNN(torch.nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=5, kernel_size=3, stride=2, padding=1)

    def forward(self, x):
        y = self.conv1(x)
        return y

cnn = CNN()

print(cnn)

# for w in cnn.parameters():
#     print(w.size())
x = np.ones((1,3,20,20))
x = x.astype(np.float32)
x = torch.from_numpy(x)
print(x.size())
y = cnn(x)
print(y.size())