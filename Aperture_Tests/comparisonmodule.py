# Copyright 2019 Merlin Hoffman
# This code compares a reconstructed image to an original image

import numpy as np
import matplotlib.pyplot as plt

orig = np.load('farfieldimage.npy')
recon = np.load('reconstructedimage.npy')

#error = lambda x,x0: (x-x0)**2

#er = error(orig,recon)

plt.imshow(orig)
plt.show()