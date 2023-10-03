#5) แปลงภาพผลลัพธ์กลับมายัง Spatial Domain
import numpy as np
import cv2 as cv

img = cv.imread('./Classwork/classwork4/test.jpg', cv.IMREAD_GRAYSCALE)

filter_h = 3
filter_w = 3
filter = np.zeros([filter_h, filter_w], dtype = np.float32)
filter[0,0] = 1; filter[0,1] = 0; filter[0,2] = -1
filter[1,0] = 2; filter[1,1] = 0; filter[1,2] = -2 
filter[2,0] = 1; filter[2,1] = 0; filter[2,2] = -1

padding = np.pad(filter, [(0, img.shape[0]-3), (0, img.shape[1]-3)], mode='constant')
freq = np.fft.fft2(padding)
imgF = np.fft.fft2(img)
conclusion = freq * imgF

#conclusion img
conclusion_inverse = np.fft.ifft2(conclusion)
output = np.real(conclusion_inverse)
img_conclusion = cv.normalize(output, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)

# sobel x
img_sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize= 5)
img_sobelx = cv.normalize(img_sobelx, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)

freq = np.fft.fft2(padding)

final_img = cv.hconcat([img_sobelx, img_conclusion])


cv.imwrite("./Classwork/classwork4/5_result.png", final_img)