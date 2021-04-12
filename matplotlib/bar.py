import matplotlib.pyplot as plt 
import numpy as np 

n = 12
x = np.arange(n)
y1 = (1-x/float(n)) * np.random.uniform(0.5, 1, n)
y2 = (1-x/float(n)) * np.random.uniform(0.5, 1, n)

plt.bar(x, +y1, facecolor='#9999ff', edgecolor='white')
plt.bar(x, -y2, facecolor='#ff9999', edgecolor='white')
for x_, y_ in zip(x, y1):
    plt.text(x_, y_+0.05, '%.2f'%y_, ha='center', va='bottom')
for x_, y_ in zip(x, y2):
    plt.text(x_, -y_-0.05, '-%.2f'%y_, ha='center', va='top')

plt.xlim(-.5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())

plt.show()