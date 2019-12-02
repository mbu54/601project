# Copyright 2019
"""
Main module for all coded aperture testing
"""

import numpy as np
import far_field_test as ff
import midfieldtest as mf
import comparison_module as comp

def main_test(coded_mask):

  # load images
  imageff = 'farfieldimage.npy'
  imagemf = 'midfieldimage.npy'

  # run far field
  recon_imageff = ff.farfield(imageff,coded_mask)

  # run mid field
  recon_imagemf = mf.midfield(imagemf,coded_mask)

  # find error
  eff = comp.compare(imageff,recon_imageff)
  emf = comp.compare(imagemf,recon_imagemf)

  print("Farfield Test Error:",eff)
  print("Midfield Test Error:",emf)


main_test('randomCM.npy')