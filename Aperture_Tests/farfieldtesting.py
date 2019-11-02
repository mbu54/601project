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

# Tikihonov reconstruction function
Tk = lambda G,H,u: Ft((np.conj(H)*G)  / (abs(H)**2 + u))

# Next we pull the CA, where the name if the file is the aperture received

CA = np.load('randomCM.npy')
'''
psf = np.zeros((N,N))
psf[49][49] = 1
psf[49][50] = 1
psf[50][49] = 1
psf[50][50] = 1
'''
# Generating the image signal
tfCA = F(CA)
g = Ft(F(obj)*tfCA)
G = F(g)
#img = F(img_sig)
u = np.logspace(-20,0,5)

#for i in range(len(u)):
f_tk = Tk(G, tfCA, u[0])

np.save("reconstructedimage.npy",f_tk)

#plt.figure(i)
#plt.imshow(abs(f_tk)

#plt.show()
'''
fig, ax = plt.subplots(1,3)

ax[0].imshow(obj)
ax[1].imshow(CA)
ax[2].imshow(abs(f_tk))

plt.show()
'''