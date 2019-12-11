# This script converts a .npy file version of a
# coded aperture mask into a .png image of said mask,
# the .npy file you want to convert must be in the
# same path as this file

import numpy as np
import matplotlib.pyplot as plt

def png_converter(file):   
  img_array = np.load(file)
  plt.imshow(img_array, cmap='gray')
  png_file = file.replace('.npy', '.png')
  plt.savefig(png_file)


file = input("Enter the name of the file you would like to convert (must in same filepath as this function): ")
png_converter(file)
