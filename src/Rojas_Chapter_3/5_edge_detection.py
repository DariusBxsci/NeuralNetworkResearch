from scipy import misc
from scipy import signal
import matplotlib.pyplot as plt

IMG_NAME = input('Enter the filename of the input image: ')
image = misc.imread(IMG_NAME,'L')

plt.imshow(image,cmap='gray')
plt.show()

cimage = signal.convolve2d([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]],image,'valid')

plt.imshow(cimage,cmap='gray')
plt.show()
