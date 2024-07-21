import cv2
import numpy as np
from matplotlib import pyplot as plt

inputImg='image.jpg'
img=cv2.imread(inputImg,-1)
cv2.imshow('Image',img)

color=('b','g','r')

for channel,col in enumerate(color):
    histr=cv2.calcHist([img],[channel],None,[256],[0,256])
    plt.plot(histr,color=col)
    plt.xlim(0,256)
plt.title('Histogram for color scale picture')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()