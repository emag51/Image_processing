import cv2 as cv
import numpy as np

img_in = cv.imread('./Class02/dark/dark.jpg', cv.IMREAD_GRAYSCALE)


gamma = 1
gamma_corrected = (img_in / 30)**gamma
gamma_corrected = gamma_corrected*200

img_out= np.array(gamma_corrected, dtype = "uint8")

cv.imshow('power_law', img_out)

cv.imwrite('./Class02/dark/dark_in.png', img_in)
cv.imwrite('./Class02/dark/dark_out.png', img_out)