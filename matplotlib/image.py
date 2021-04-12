import matplotlib.pyplot as plt 
import numpy as np 
import cv2 

image = cv2.imread('1.jpg')
# cv2.imshow('img', image)
# cv2.waitKey(0)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# image = image[::-1,:,:]

plt.imshow(image, interpolation='nearest', cmap=plt.cm.bone, origin='upper')
plt.colorbar(shrink=0.9)

plt.xticks(())
plt.yticks(())
plt.show()