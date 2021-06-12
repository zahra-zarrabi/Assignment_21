import cv2

image = cv2.imread("3.jpg")
image = cv2.resize(image, (600, 500))
image=cv2.rotate(image,cv2.ROTATE_180)
cv2.imshow("show output",image)
cv2.waitKey()