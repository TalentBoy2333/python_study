import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(-3,3,50)
# print(x)
y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('x')
plt.ylabel('y')

l1, = plt.plot(x, y1, label='up')
l2, = plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--', label='dowm')
plt.legend(handles=[l1, l2, ], labels=['ups', 'downs'], loc='best')

plt.show()