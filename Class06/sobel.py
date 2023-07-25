import numpy as np
import cv2 as cv

img = cv.imread('./Class06/test.jpg', cv.IMREAD_GRAYSCALE)

laplacian = cv.Laplacian(img, cv.CV_64F)
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize= 5)
sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize= 5)

print('[Input] type:', img.dtype)
print('[Laplacian] type:', laplacian.dtype)
print('[Sobel X] type', sobelx.dtype)
print('[Sobel Y] type', sobely.dtype)

cv.imwrite('./Class06/laplacian.png', laplacian)
cv.imwrite('./Class06/sobelx.png', sobelx)
cv.imwrite('./Class06/sobely.png', sobely)