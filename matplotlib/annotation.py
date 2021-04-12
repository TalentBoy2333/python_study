import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(-3,3,50)
# print(x)
y = 2*x + 1

plt.figure()
# plt.xlim((-4,4))
# plt.ylim((-6,8))
plt.xlabel('x')
plt.ylabel('y')

ax = plt.gca()
ax.spines['right'].set_color(None)
ax.spines['top'].set_color(None)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

plt.plot(x, y)

x0 = 1
y0 = 2*x0 + 1
plt.scatter(x0, y0, s=50, color='b')
plt.plot([x0,x0], [y0,0], 'k--', lw=2.5)

# method 1
#######################
plt.annotate(r'$2x+1=%s$'%y0, xy=(x0,y0), xycoords='data', xytext=(+30,-30), 
            textcoords='offset points', fontsize=16, 
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))

# method 2
######################
plt.text(-3.6, 3, r'$This\ is\ the\ some\ text.\ \mu\ \theta_i\ \alpha^t$', 
        fontdict={'size':16, 'color':'r'})

plt.show()