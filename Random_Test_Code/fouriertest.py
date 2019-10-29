# Merlin Hoffman
# Fouier Optics Stuff

import numpy as np
import matplotlib.pyplot as plt

# this is for a single square signal centered at 0
'''
zeropad = np.zeros(124)
a_small = np.array([1,1,1,1,1,1,1,1,1],dtype=float)
a = np.concatenate((zeropad,a_small,zeropad))
'''
# This is a bunch repeating square waves
# different widths shown for compareing examples
'''
timestep = 0.0001
a = np.array([],dtype=float)
for i in range(500):
  a = np.append(a,[0,1,0,0,0,0,0,0,0,0,0])

b = np.array([],dtype=float)
for i in range(500):
  b = np.append(b,[0,1,1,1,1,0,0,0,0,0,0])


A = np.fft.fft(a)
B = np.fft.fft(b)
n = a.size
freq = np.fft.fftfreq(n,d=timestep)

plt.plot(freq,A.real,freq,B.real)
plt.show()
'''
# 2D fourier transforms for screens

width = 10
imagewidth = 81

a = np.zeros((imagewidth,imagewidth))
for i in range((imagewidth//2)//width):
  for j in range((imagewidth//2)//width):
    for k in range(width+1):
      for l in range(width+1):
        a[i*2*width+k][j*2*width+l] = 1

A = np.fft.fft2(a)
A = np.fft.fftshift(A)

width = 4

b = np.zeros((imagewidth,imagewidth))
for i in range((imagewidth//2)//width):
  for j in range((imagewidth//2)//width):
    for k in range(width+1):
      for l in range(width+1):
        b[i*2*width+k][j*2*width+l] = 1

B = np.fft.fft2(b)
B = np.fft.fftshift(B)

width = 20
imagewidth = 81

c = np.zeros((imagewidth,imagewidth))
for k in range(width):
  for l in range(width):
    c[31+k][31+l] = 1

plt.rc('image',cmap='gray_r')
fig1, ax1 = plt.subplots(1,2)
fig2, ax2 = plt.subplots(1,2)
fig3, ax3 = plt.subplots(1,2)
for i in range(2):
  ax1[i].set_xticks([])
  ax1[i].set_yticks([])
  ax2[i].set_xticks([])
  ax2[i].set_yticks([])
  ax3[i].set_xticks([])
  ax3[i].set_yticks([])
ax1[0].imshow(a)
ax1[0].title.set_text('Larger Mesh Pattern')
ax1[1].imshow(abs(A))
ax1[1].title.set_text('Larger Mesh Pattern Ft')
ax2[0].imshow(b)
ax2[0].title.set_text('Smaller Mesh Pattern')
ax2[1].imshow(abs(B))
ax2[1].title.set_text('Smaller Mesh Pattern Ft')

ai = np.fft.ifft2(A)
fA = A*c
fai = np.fft.ifft2(fA)
ax3[0].imshow(abs(ai))
ax3[0].title.set_text('Mesh Pattern iFt')
ax3[1].imshow(abs(fai))
ax3[1].title.set_text('Filtered Mesh Pattern iFt')

plt.show()


# fourier transform for grating
# didn't finish -> this doesn't work
'''
disstep = 0.1
wvlgth = 632.8*10**-9
T = (1*10**-3)/80
theta = wvlgth/T
n = 40
dis = np.linspace(-n*disstep,n*disstep,num=(2*n+1))
m = 10

grating = np.zeros(2*n+1)
for j in range(-2,3):
  grating[n+m*j] = 1

plt.plot(dis,grating)
plt.show()
'''
'''
width = 10
imagewidth = 101

c = np.zeros((imagewidth,imagewidth))
for k in range(width):
  for l in range(width):
    c[46+k][46+l] = 1

C = np.fft.fft2(c)
C = np.fft.fftshift(C)
ci = np.fft.ifft2(C.real)

fig3, ax3 = plt.subplots(1,2)
ax3[0].imshow(c)
ax3[1].imshow(abs(ci))
plt.show()
'''