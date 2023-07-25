# import the two modules
import cv2 as cv
import numpy as np
# load path of the image
img = cv.imread("./Class04/noise.png")
# create a sharpening kernel
sharpen_filter=np.array([[-1,-1,-1],
                 [-1,9,-1],
                [-1,-1,-1]])
# applying kernels to the input image to get the sharpened image
sharp_image=cv.filter2D(img,-1,sharpen_filter)
cv.imwrite('./Class04/notblur.png',sharp_image)