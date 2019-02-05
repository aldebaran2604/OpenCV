import cv2

def mouse_drawing(event, x, y, flags, params):
    print("Left click")

image = cv2.imread("clouds.jpg")


cv2.imshow("Over the Clouds", image)
cv2.setMouseCallback("Over the Clouds", mouse_drawing)
while(True):
    key = cv2.waitKey(1)
    print(key)
cv2.destroyAllWindows()