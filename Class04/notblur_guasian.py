# import the two modules
import cv2 as cv
# load path of the image
img = cv.imread("./Class04/noise.png")
# create a sharpening kernel
for i in range (0, 5):
    blur = cv.medianBlur(img, i)
    cv.imwrite('./Class04/{i}.png',blur)