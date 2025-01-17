import cv2
import numpy as np
from matplotlib import pyplot as plt

inputImg='gray.png'

gray_img=cv2.imread(inputImg,cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',gray_img)

hist=cv2.calcHist([gray_img],[0],None,[256],[0,256])

plt.hist(gray_img.ravel(),256,[0,256])
plt.title('Histogram for gray scale picture')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()