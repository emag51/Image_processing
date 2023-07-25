# 3) แปลง Filter Sobel ให้อยู่ใน Frequency Domain ด้วย Fourier Transform
import numpy as np
import cv2 as cv

img = cv.imread('./classwork4/test.jpg', cv.IMREAD_GRAYSCALE)
print(img.shape)
# (350,750)

filter_h = 3
filter_w = 3
filter = np.zeros([filter_h, filter_w], dtype = np.float32)
filter[0,0] = 1; filter[0,1] = 0; filter[0,2] = -1
filter[1,0] = 2; filter[1,1] = 0; filter[1,2] = -2 
filter[2,0] = 1; filter[2,1] = 0; filter[2,2] = -1

padding = np.pad(filter, [(0, img.shape[0]-3), (0, img.shape[1]-3)], mode='constant')

freq = np.fft.fft2(padding)

imgReal = np.real(freq)
imgIma = np.imag(freq)
imgMag = np.sqrt(imgReal**2 + imgIma**2)
imgMag = np.log(1+imgMag)
filter_img = cv.normalize(imgMag, None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8U)

cv.imwrite("./classwork4/3_result.png", filter_img)