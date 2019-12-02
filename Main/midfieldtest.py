# Mid-field test example

import numpy as np
import matplotlib.pyplot as plt

def midfield(image,coded_mask):

	obj = np.load(image)
	# N = np.size(obj, 1)

	# Fourier Transform functions

	F = lambda x: np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(x)))
	Ft = lambda x: np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(x)))

	# Tikihonov reconstruction function

	Tk = lambda G,H,u: Ft((np.conj(H)*G)  / (abs(H)**2 + u))

	# Pulling CA

	CA = np.load(coded_mask)

	# Generating the image signal
	tfCA = F(CA)
	g = Ft(F(obj)*tfCA)
	G = F(g)
	#img = F(img_sig)
	u = np.logspace(-20,0,5)

	#for i in range(len(u)):
	f_tk = Tk(G, tfCA, u[0])

	# np.save("reconstructedimage.npy",f_tk)

	'''plt.imshow(abs(f_tk))
	plt.show()'''

	fig, ax = plt.subplots(1,3)
	ax[0].imshow(obj)
	ax[1].imshow(CA)
	ax[2].imshow(abs(f_tk))
	plt.show()
