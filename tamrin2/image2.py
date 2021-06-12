import cv2

image = cv2.imread("2.jpg")

img = cv2.resize(image, (600, 500))
rows = img.shape[0]
cols = img.shape[1]
for i in range(rows):
    for j in range(cols):
        img[i, j] = 255 - img[i, j]

cv2.imshow("show output", img)
cv2.waitKey()