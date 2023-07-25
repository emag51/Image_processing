import cv2 as cv
import numpy as np

img_input = cv.imread('./Class03/pic02.jpg', cv.IMREAD_GRAYSCALE)

filterSize = 50

kernel = np.ones((filterSize, filterSize), np.float32)/(filterSize**2)

output = cv.filter2D(img_input, -1, kernel, borderType= cv.BORDER_REFLECT)

cv.imwrite('./Class03/pic02.jpg', img_input)
cv.imwrite('./Class03/output.jpg', output)
