# 1) สร้าง Sobel Filter แบบ Horizontal หรือ Vertical อย่างใดอย่างหนึ่งใน Spatial Domain
import numpy as np
import cv2 as cv

img = cv.imread('./Classwork4/test.jpg', cv.IMREAD_GRAYSCALE)

sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize= 5)
sobelx = cv.normalize(sobelx, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)

cv.imwrite('./Classwork4/1_result.png', sobelx)