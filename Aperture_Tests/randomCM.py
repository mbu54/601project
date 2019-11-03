# Copyright 2019 Merlin Hoffman
# This code makes a random array coded mask
# The total mask is 100x100 pixels
# The size of each box is 5x5 pixels
# Each box is randomly picked each time the code is run

import numpy as np
import random
import matplotlib.pyplot as plt

maskWidth = 100
boxWidth = 5 # must divde maxWidth without a remainder

mask = np.zeros((maskWidth,maskWidth))
for i in range(0,maskWidth,boxWidth):
  for j in range(0,maskWidth,boxWidth):
    rand = random.random()
    if rand >= 0.98:
      for k in range(boxWidth):
        for l in range(boxWidth):
          mask[i+k][j+l] = 1

np.save('randomCM.npy',mask)
'''
masktest = np.load('randomCM.npy') # test load

plt.imshow(masktest) # plots mask
plt.show()
'''