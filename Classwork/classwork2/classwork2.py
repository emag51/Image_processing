import cv2 as cv
import numpy as np

img = cv.imread('./Classwork/classwork2/test.jpg', cv.IMREAD_GRAYSCALE)
gray = cv.cvtColor(img, cv.IMREAD_GRAYSCALE)
blur = cv.medianBlur(gray,5)
edges = cv.Canny(blur,230,255)
for row in range(0,img.shape[0],3):
    for col in range(0,img.shape[1],3):
        pixel = edges[row, col]
        if pixel > 230:
            #print(pixel)
            radius = 60  
            cv.circle(img, (col, row), radius, (0, 255,0),1 )
            

cv.imwrite('./Classwork/classwork2/output_2.png', img)