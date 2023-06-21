import cv2 as cv
import numpy as np

img_in = cv.imread('./Class02/light/light.jpg', cv.IMREAD_GRAYSCALE)


gamma = 10
gamma_corrected = (img_in / 255)**gamma
gamma_corrected = gamma_corrected*255

img_out= np.array(gamma_corrected, dtype = "uint8")

cv.imshow('power_law', img_out)

cv.imwrite('./Class02/light/light_in.png', img_in)
cv.imwrite('./Class02/light/light_out.png', img_out)