# Copyright 2019
'''
This code compares a reconstructed image to an original image
'''
import numpy as np

def compare(image,recon_image):
  
  # define error function to sum difference between new and original
  error = lambda x,x0: np.sum(abs((x-x0)**2))
  # 0 is a perfect reconstruction
  # larger error is a worse reconstruction

  # load original and reconstructed images
  orig = np.load(image)
  recon = np.load(recon_image)

  # calculate error
  e = error(recon,orig)

  return e
