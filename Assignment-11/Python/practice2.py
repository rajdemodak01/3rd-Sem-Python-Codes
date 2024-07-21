import cv2
import numpy
from matplotlib import pyplot

image1=cv2.imread('gray.png',cv2.IMREAD_GRAYSCALE)
image2=cv2.equalizeHist(image1)

cv2.imshow("image1",image1)
cv2.imshow("image2",image2)

hist1=cv2.calcHist([image1],[0],None,[256],[0,256])
pyplot.plot(hist1)
pyplot.show()

hist2=cv2.calcHist([image2],[0],None,[256],[0,256])
pyplot.plot(hist2)
pyplot.show()


cv2.waitKey(0)
cv2.destroyAllWindows()