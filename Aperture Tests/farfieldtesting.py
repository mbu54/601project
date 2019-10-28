# Here is were we attempt to create a far-field test for CAs

import numpy as np
import scipy

''' Currently working on setting up code for transforming
signals. This code will only have tests for far field. '''

# We begin with establishing the Fourier Transform functions

F = lambda x: np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(x)))
Ft = lambda x: np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(x)))

# Next we pull the CA

CA()

# Creating the PSF

PSF = np.zeros(N, N)

# Creating the impulse response

H_omega = F()

''' This code is currently under major edits. It is likely
that the FTs and setups will be established as a separate
code that the tests call upon.'''