import numpy as np
import megengine as mge
from megengine.optimizer import SGD
from megengine.autodiff import GradManager
import megengine.functional as F
from loguru import logger

from network import LeNet
from data import train_dataloader

net = LeNet()

optimizer = SGD(net.parameters(), lr=0.01, momentum=0.9, weight_decay=5e-4)

gm = GradManager().attach(net.parameters())

net.train()
total_epochs = 5
for epoch in range(total_epochs):
    total_loss = 0
    for step, (batch_data, batch_label) in enumerate(train_dataloader):
        batch_data = mge.tensor(batch_data)
        batch_label = mge.tensor(batch_label).astype(np.int32)

        with gm:
            pred = net(batch_data)
            loss = F.loss.cross_entropy(pred, batch_label)
            gm.backward(loss)
        optimizer.step().clear_grad()

        total_loss += loss.numpy().item()
        if step % 100 == 0: 
            logger.info("epoch: {}, iter: {}, loss {}".format(epoch, step, total_loss/len(train_dataloader)))
    logger.info("epoch: {}, loss {}".format(epoch, total_loss/len(train_dataloader)))

mge.save(net.state_dict(), 'mnist_net.mge')