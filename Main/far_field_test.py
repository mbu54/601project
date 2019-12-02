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
  # N = np.size(orig_image, 1) # get size of original image (should be 100x100)
  
  # set mu and deviation
  sigma = 5

  # convolve mask with orig_image
  MASK = F(mask) 
  g = invF(F(orig_image)*MASK) # output image from convolution
  g_n = sigma*np.random.randn(g.shape[0],g.shape[1]) + g # add noise to image
  G = F(g) # Fourier transform of output image
  G_n = F(g_n) #Fourier transform of output image with noise


  # select regulariztion parameters to try
  u = np.logspace(2,5,4) #np.logspace(-20,0,5)
  recon_image = []
  for i in range(u.size):
    recon_image.append(Tikhonov(G_n, MASK, u[i]))

  np.save('reconstructedimageff.npy',recon_image[1]) # save reconstructed image

  # plot image
  fig, ax = plt.subplots(2,2)
  
  ax[0][0].imshow(abs(recon_image[0]))
  ax[0][1].imshow(abs(recon_image[1]))
  ax[1][0].imshow(abs(recon_image[2]))
  ax[1][1].imshow(abs(recon_image[3]))
  
  '''
  ax[0][0].imshow(orig_image)
  ax[0][1].imshow(mask)
  ax[1][0].imshow(abs(g_n))
  ax[1][1].imshow(abs(recon_image[2]))
  '''
  plt.show()

  return 'reconstructedimageff.npy'
  
#farfield('farfieldimage.npy','randomCM.npy')