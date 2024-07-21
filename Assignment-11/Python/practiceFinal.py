import cv2
import matplotlib.pyplot as plt

image1=cv2.imread('gray.png',cv2.IMREAD_GRAYSCALE)
image2=cv2.equalizeHist(image1)
cv2.imshow('image',image2)

hist=cv2.calcHist([image2],[0],None,[256],[0,256])
plt.plot(hist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()