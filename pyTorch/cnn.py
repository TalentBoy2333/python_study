import torch 
from torch.autograd import Variable 
import torch.utils.data as Data 
import torchvision 
import matplotlib.pyplot as plt 

EPOCH = 1
BATCH_SIZE = 50
LR = 0.001
DOWNLOAD_MNIST = False 

train_data = torchvision.datasets.MNIST(
    root='./mnist',
    train=True,
    transform=torchvision.transforms.ToTensor(),
    download=DOWNLOAD_MNIST
)

print(train_data.train_data.size())
print(train_data.train_labels.size())
# plt.imshow(train_data.train_data[0].numpy(), cmap='gray')
# plt.title('%i' % train_data.train_labels[0])
# plt.show()

train_loader = Data.DataLoader(
    dataset=train_data, 
    batch_size=BATCH_SIZE, 
    shuffle=True, 
    num_workers=2
)

test_data = torchvision.datasets.MNIST(
    root='./mnist',
    train=False
)
test_x = Variable(torch.unsqueeze(test_data.test_data, dim=1)).type(torch.FloatTensor)[:2000]/255.
test_y = test_data.test_labels[:2000]
print(test_x.data.numpy().shape)
print(test_y.data.numpy().shape)

class CNN(torch.nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = torch.nn.Sequential(
            torch.nn.Conv2d(in_channels=1, out_channels=16, kernel_size=5, stride=1, padding=2),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2),
        )
        self.conv2 = torch.nn.Sequential(
            torch.nn.Conv2d(16, 32, 5, 1, 2),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2)
        )
        self.out = torch.nn.Linear(32*7*7, 10)

    def forward(self, x): # (batch, 28, 28, 1)
        x = self.conv1(x) # (batch, 14, 14, 16)
        x = self.conv2(x) # (batch, 7, 7, 32)
        x = x.view(x.size(0), -1) # (batch, 7*7*32)
        output = self.out(x)
        return output

cnn = CNN()
# print(cnn)

optimizer = torch.optim.Adam(cnn.parameters(), lr=LR)
loss_func = torch.nn.CrossEntropyLoss()

# for step, (x,y) in enumerate(train_loader):
#     b_x = Variable(x)
#     b_y = Variable(y)
#     output = cnn(b_x)
#     print(b_y.shape)
#     print(output.shape)

for epoch in range(EPOCH):
    for step, (x,y) in enumerate(train_loader):
        b_x = Variable(x)
        b_y = Variable(y)
        # b_x = x
        # b_y = y
        output = cnn(b_x)
        loss = loss_func(output, b_y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if step % 50 == 0:
            test_output = cnn(test_x)
            pred_y = torch.max(test_output, 1)[1].data.squeeze()
            right = 0
            for i in range(2000):
                if pred_y.data[i] == test_y.data[i]:
                    right += 1
            accuracy = right/2000.
            # print(pred_y)
            # print(test_y)
            # print(sum(pred_y.data == test_y.data).type(torch.FloatTensor))
            # print(test_y.shape[0])
            # accuracy = sum(pred_y == test_y).type(torch.FloatTensor) / test_y.shape[0]
            # print(accuracy.data.numpy())
            print('Epoch:', epoch, '| train loss: %.4f' % loss.data.numpy(), '| test accuracy:', accuracy)

test_output = cnn(test_x[:10])
pred_y = torch.max(test_output, 1)[1].data.numpy().squeeze()
print(pred_y, 'prediction number')
print(test_y[:10].numpy(), 'real number')

