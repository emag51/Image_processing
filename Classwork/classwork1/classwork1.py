import cv2 as cv
import numpy as np

img = cv.imread('./Classwork/classwork1/test.jpg', cv.IMREAD_GRAYSCALE)
img = cv.resize(img,(600,600))

size = 20

filter_motionblur = np.zeros((size, size))
# vertical
filter_motionblur[:, int((size - 1)/2)] = np.ones(size) 

#horicontal
#filter_motionblur[int((size-1)/2), :] = np.ones(size)

#ทะแยงซ้ายไปขวา
#filter_motionblur = np.eye(20, dtype=np.float32) 

#ทะแยงขวาไปซ้าย
# for i in range(size):
#   filter_motionblur[i, size - 1 - i] =  1  

filter_motionblur = filter_motionblur / size
print(filter_motionblur)
output = cv.filter2D(img, -1, filter_motionblur)

cv.imwrite('./Classwork/classwork1/output_1.png', output)