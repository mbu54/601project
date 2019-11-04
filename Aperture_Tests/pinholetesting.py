import numpy as np
import matplotlib.pyplot as plt

'''
This test is used for experimentally getting a control for the image output by
showing how it works against a pinhole setup.
'''
# Load the image sample

obj = np.load('farfieldimage.npy')
N = np.size(obj, 1)

# Establish the Fourier Transform functions

F = lambda x: np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(x)))
Ft = lambda x: np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(x)))

# Testing against a pinhole with dimensions 100 x 100

PSF = np.zeros((100,100))
PSF[49][49] = 1

# Generating the image signal

img_sig = Ft(F(obj) * F(PSF))

img = F(img_sig)

plt.imshow(abs(img))
plt.show()