import numpy as np
import cv2

kernel = 5

img = cv2.imread('./Class06/test.jpg',cv2.IMREAD_GRAYSCALE)

lowPass = cv2.filter2D(img,-1, kernel)
lowPass = img - lowPass

cv2.imwrite('./Class06/freq.png',np.hstack((img, lowPass)))