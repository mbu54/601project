# Copyright 2019 Merlin Hoffman
# This code compares a reconstructed image to an original image

import numpy as np
import matplotlib.pyplot as plt

orig = np.load('farfieldimage.npy')
recon = np.load('reconstructedimage.npy')

err = lambda x,x0: np.sum(abs((x-x0)**2))

er = err(orig,orig)

print(er)