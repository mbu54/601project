# Mid-field test example

import numpy as np
import matplotlib.pyplot as plt

obj = np.load('midfieldimage.npy')
N = np.size(obj, 1)

# Fourier Transform functions

F = lambda x: np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(x)))
Ft = lambda x: np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(x)))

# Tikihonov reconstruction function

Tk = lambda G,H,u: Ft((np.conj(H)*G)  / (abs(H)**2 + u))

# Pulling CA

CA = np.load('randomCM.npy')

# Generating the image signal
tfCA = F(CA)
g = Ft(F(obj)*tfCA)
G = F(g)
#img = F(img_sig)
u = np.logspace(-20,0,5)

#for i in range(len(u)):
f_tk = Tk(G, tfCA, u[0])

# np.save("reconstructedimage.npy",f_tk)

plt.imshow(abs(f_tk))
plt.show()