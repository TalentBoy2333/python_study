import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(-3,3,50)
y1 = 2*x + 1
y2 = x**2


plt.figure()
plt.plot(x, y1)

plt.figure(num=3, figsize=(8,5))
plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--')
plt.plot(x, y1)

fig = plt.figure()
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax1 = fig.add_axes([left, bottom, width, height])
ax1.plot(x, y1, 'b')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

plt.show()