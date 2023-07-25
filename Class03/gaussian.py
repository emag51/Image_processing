import cv2 as cv
import numpy as np

img_input = cv.imread('./Class03/pic02.jpg', cv.IMREAD_GRAYSCALE)

ksize = (31, 31)
sigmaX = 10.0

output = cv.GaussianBlur(img_input, ksize, sigmaX, borderType= cv.BORDER_REFLECT)

cv.imwrite('./Class03/pic02.jpg', img_input)
cv.imwrite('./Class03/output.jpg', output)
