# Copyright 2019
"""
Main module for all coded aperture testing
"""

import numpy as np
import far_field_test as ff
import comparison_module as comp

def main_test(coded_mask):

  # load image
  image = 'farfieldimage.npy'

  # run far field
  recon_image = ff.farfield(image,coded_mask)

  # run error
  e = comp.compare(image,recon_image)

  print(e)


main_test('randomCM.npy')