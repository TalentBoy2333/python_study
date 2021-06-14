import numpy as np 
import megengine as mge
import megengine.functional as F

from data import test_dataloader
from network import LeNet

net = LeNet()
state_dict = mge.load('mnist_net.mge')
net.load_state_dict(state_dict)

net.eval()
correct = 0
total = 0
for idx, (batch_data, batch_label) in enumerate(test_dataloader):
    batch_data = mge.tensor(batch_data)
    batch_label = mge.tensor(batch_label).astype(np.int32)

    pred = net(batch_data)
    loss = F.loss.cross_entropy(pred, batch_label)
    predicted = pred.numpy().argmax(axis=1)
    correct += (predicted == batch_label.numpy()).sum().item()
    total += batch_label.shape[0]
print("correct: {}, total: {}, accuracy: {}".format(correct, total, float(correct) / total))