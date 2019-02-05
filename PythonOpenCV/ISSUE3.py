import cv2

image = cv2.imread("clouds.jpg")

cv2.imwrite('clouds2.png',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

