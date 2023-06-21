import cv2 as cv
import numpy as np

img_input = cv.imread('dark.jpg', cv.IMREAD_GRAYSCALE)

img_output = np.log(img_input)

img_max = np.max(img_output)
img_output = img_output*(255/ img_max)

img_output = np.array(img_output, dtype = np.uint8)

cv.imwrite('dark.png', img_output)
cv.imwrite('OUTPUT', img_output)