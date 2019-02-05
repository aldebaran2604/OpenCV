import cv2
import numpy as np

image = cv2.imread('clouds.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

increase = 255

v = image[:, :, 2]
v = np.where(v <= 255 - increase, v + increase, 255)
image[:, :, 2] = v

image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)

cv2.imshow('Brightness', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
