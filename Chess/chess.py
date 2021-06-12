import numpy as np
import cv2
x=160
y=160
flag=True
img= np.zeros((x, y), dtype="uint8")
for m in range(0, x, 20):
    flag=not flag
    for n in range(0, y, 20):
        if flag:
            flag=False
            img[m:m+20, n:n+20] = np.zeros((20, 20))

        else:
            img[m:m+20, n:n+20] = np.ones((20, 20))*255
            flag=True
cv2.imshow('Show output', img)
cv2.imwrite('out.jpg', img)
cv2.waitKey()