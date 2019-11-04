# Copyright 2019

"""
This code reconstructs an image in the far field with a coded aperture
"""

import numpy as np
import matplotlib.pyplot as plt

def farfield(image,coded_mask):

  # define funcitons for iamgeing
  F = lambda x: np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(x))) # takes Fourier Transform
  invF = lambda x: np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(x))) # takes Inverse Fourier Transform
  Tikhonov = lambda G,H,u: invF((np.conj(H)*G)  / (abs(H)**2 + u)) # does Tikhonov construction (see below for info)
  # G is Fourier Transform of convolution between Image and coded mask
  # H is Fourier Transform of coded mask
  # u is the regularization parameter which balances approximation error and noise progation error

  orig_image = np.load(image) # load npy file of image
  mask = np.load(coded_mask) # load npy file of mask
  #N = np.size(orig_image, 1) # get size of original image (should be 100x100)
  
  # convolve mask with orig_image
  MASK = F(mask) 
  g = invF(F(orig_image)*MASK) # output image from convolution
  G = F(g) # Fourier transform of output image

  # select regulariztion parameters to try
  u = np.logspace(-20,-10,5) #np.logspace(-20,0,5)

  recon_image = Tikhonov(G, MASK, u[0])

  np.save('reconstructedimageff.npy',recon_image) # save reconstructed image

  return 'reconstructedimageff.npy'
  '''
  # plot image
  fig, ax = plt.subplots(2,2)

  ax[0][0].imshow(orig_image)
  ax[0][1].imshow(mask)
  ax[1][0].imshow(abs(g))
  ax[1][1].imshow(abs(recon_image))

  plt.show()
  '''
#farfield('farfieldimage.npy','randomCM.npy')