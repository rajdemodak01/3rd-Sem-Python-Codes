import cv2
from matplotlib import pyplot

image='image.jpg'

image=cv2.imread('image.jpg')
cv2.imshow("image",image)

hist=cv2.calcHist([image],[0],None,[256],[0,256])
pyplot.plot(hist)
pyplot.show()

cv2.waitKey(0)
cv2.destroyAllWindows()