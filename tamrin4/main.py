import cv2

image = cv2.imread("4.jpg")
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

img = cv2.resize(image, (600, 500))
rows=img.shape[0]
cols=img.shape[1]
for i in range(rows):
    for j in range(cols):
        if img[i,j] > 70:
            img[i,j]=255
        else:
            img[i,j]=img[i,j]

cv2.imshow("show output",img)
cv2.waitKey()