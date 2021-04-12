import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(-3,3,50)
# print(x)
y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.plot(x, y1)
plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--')

plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('x')
plt.ylabel('y')

new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, 0, 1, 3], 
            [r'$really\ bad$', 'bad', r'$\alpha$', 'good', 'really good'])

# gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color(None)
ax.spines['top'].set_color(None)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

plt.show()