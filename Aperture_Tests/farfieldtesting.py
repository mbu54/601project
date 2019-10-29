# Here is were we attempt to create a far-field test for CAs

import numpy as np
import matplotlib.pyplot as plt

''' Currently working on setting up code for transforming
signals. This code will only have tests for far field. '''

''' Importing our object as an array
We will need to create a file (farfieldimage) that
holds the array that represents the image for the far-field
test'''

obj = np.load('farfieldimage.npy')
N = np.size(obj, 1)

# We begin with establishing the Fourier Transform functions

F = lambda x: np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(x)))
Ft = lambda x: np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(x)))

# Next we pull the CA, where the name if the file is the aperture received

CA = np.load('randomCM.npy')

# Generating the image signal

img_sig = Ft(F(obj) * F(PSF))

img = F(img_sig)

plt.imshow(abs(img))
plt.show()
