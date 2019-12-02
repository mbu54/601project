'''
This code makes a star input image to test 
coded masks for mid-field
'''

import numpy as np
import matplotlib.pyplot as plt

imageWidth = 200
c = imageWidth//2-1

image = np.zeros((imageWidth,imageWidth))
for x in range(imageWidth):
  for y in range(imageWidth):
    if (x-c)**2+(y-c)**2 <= (c//2)**2:
      if (y-c)<-0.5*(x-c) and (y-c)>-2*(x-c):
        image[x][y] = 1
      elif (y-c)>-0.5*(x-c) and (y-c)<-2*(x-c):
        image[x][y] = 1
      elif (y-c)<2*(x-c) and (y-c)>0.5*(x-c):
        image[x][y] = 1
      elif (y-c)>2*(x-c) and (y-c)<0.5*(x-c):
        image[x][y] = 1
      elif y==c and x==c:
        image[x][y] = 1

np.save('midfieldimage.npy',image)

# plot image
plt.imshow(image)
plt.show()