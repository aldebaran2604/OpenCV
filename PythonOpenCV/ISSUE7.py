import cv2

img = cv2.imread('clouds.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.equalizeHist(img)

cv2.imshow('Histogramas', img)
cv2.waitKey()
