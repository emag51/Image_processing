# 2) แปลงภาพ Input ให้อยู่ใน Frequency Domain ด้วย Fourier Transform
import numpy as np
import cv2 as cv

img = cv.imread('./classwork4/test.jpg', cv.IMREAD_GRAYSCALE)

img = img.astype(np.float32)

imgF = np.fft.fft2(img)

imgF = np.fft.fftshift(imgF)

imgReal = np.real(imgF)
imgIma = np.imag(imgF)
imgMag = np.sqrt(imgReal**2 + imgIma**2)
imgPhs = np.arctan2(imgIma, imgReal)

imgRealInv = imgMag*np.cos(imgPhs)
imgImaInv = imgMag*np.sin(imgPhs)

imgFlnv = imgRealInv + imgImaInv*1j
imgFlnv = np.fft.ifftshift(imgFlnv)
imgInv = np.fft.ifft2(imgFlnv)

imgInv = np.real(imgInv)
imgInv = imgInv.astype(np.uint8)

imgMag = np.log(1 + imgMag)
imgMag = cv.normalize(imgMag, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
cv.imwrite('./classwork4/2_result.png', imgMag)