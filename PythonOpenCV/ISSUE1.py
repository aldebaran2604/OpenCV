import cv2

image = cv2.imread("clouds.jpg")

cv2.imshow("Over the Clouds", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
