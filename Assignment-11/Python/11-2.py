import cv2
import numpy as np
from matplotlib import pyplot as plt

inputImg='gray.png'
img=cv2.imread(inputImg)
img_to_yuv=cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
img_to_yuv[:,:,0]=cv2.equalizeHist(img_to_yuv[:,:,0])
hist_equalization_result=cv2.cvtColor(img_to_yuv,cv2.COLOR_YUV2BGR)

cv2.imshow('gray',img)
output_img='result.jpg'
cv2.imwrite(output_img,hist_equalization_result)
cv2.imshow('result',hist_equalization_result)


inputImg2='result.jpg'
gray_img=cv2.imread(inputImg2,cv2.IMREAD_GRAYSCALE)
hist=cv2.calcHist([gray_img],[0],None,[256],[0,256])
plt.hist(gray_img.ravel(),256,[0,256])
plt.title('Histogram for gray scale picture')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()