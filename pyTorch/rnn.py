import torch 
import numpy as np
from torch.autograd import Variable 
import matplotlib.pyplot as plt  

start = np.random.rand(1)[0] * 90
# start = 0
# print(start)
x = torch.unsqueeze(torch.linspace(start, start+10, 100), dim=1)
y = torch.sin(x)
data_xy = torch.cat([x, y], 1)

x = Variable(x)
y = Variable(y)
data_xy = Variable(data_xy)
# print('data_xy:', data_xy.size())
# print(data_xy)

# plt.scatter(x.data.numpy(), y.data.numpy())
# plt.show()



class RNN(torch.nn.Module):
	def __init__(self):
		super(RNN, self).__init__()
		self.rnn = torch.nn.LSTM(
			input_size=2, 
			hidden_size=64, 
			num_layers=1,
			batch_first=True
		)
		self.fc = torch.nn.Linear(64, 2)
		self.fc.weight.data.normal_(0, 0.1)

	def forward(self, x):
		h_n = torch.zeros(1, 1, 64)
		c_n = torch.zeros(1, 1, 64)
		output, (h_n, c_n) = self.rnn(x, (h_n, c_n))
		# print(
		# 	'\noutput:', output.size(), 
		# 	'\nh_n:', h_n.size(), 
		# 	'\nc_n:', c_n.size(),
		# )
		output = torch.squeeze(output, dim=0)
		output = self.fc(output)

		return output

rnn = RNN()

plt.ion()
plt.show()

optimizer = torch.optim.Adam(rnn.parameters(), lr=0.001)
loss_func = torch.nn.MSELoss()



for t in range(10000):
	temp_xy = torch.unsqueeze(data_xy[0], dim=0)
	for i in range(100):
		if i == 0:
			input_xy = temp_xy
		else:
			input_xy = torch.cat([input_xy, temp_xy], 0)
	input_xy = torch.unsqueeze(input_xy, dim=0)
	# print(input_xy.size())

	pred_xy = rnn(input_xy)
	# print('pred_xy:', pred_xy.size())

	loss = loss_func(pred_xy, data_xy)
	optimizer.zero_grad()
	loss.backward()
	optimizer.step()
	if t % 100 == 0:
		print(
			'Iter:', t, 
			'| loss:', loss.data.numpy(), 
			'| learning rate:', 0.001
		)
		pred_x = pred_xy[:,0].data.numpy()
		pred_y = pred_xy[:,1].data.numpy()
		plt.cla()
		plt.scatter(x.data.numpy(), y.data.numpy(), c='g')
		plt.scatter(pred_x, pred_y)
		plt.pause(0.1)

plt.ioff()
plt.show()
