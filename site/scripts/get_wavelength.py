# legacy file 

import sys
import os
import numpy as np
import matplotlib.pylab as plt
from PIL import Image 

# binary file 
filename = 'iss.2013318.1114.155307.L1B.CCNY.v04.15181.20131114212839.100m.hico.bil'
filesize = os.path.getsize(filename) 

# bil encoding 
samples  = 500    # rows
bands    = 87     # bands
lines    = 2000   # columns
xstart   = 11     # coordinate for the upper-left hand pixel in the image          
dataSize = 2      # 16-bit signed integer (2 bytes)

stream = bytearray()
curr = xstart

hicoFile = open(filename, mode='rb'); 

while curr <= filesize: 
	hicoFile.seek(curr)
	byte     = hicoFile.read(samples * dataSize)
	stream  += byte 
	numRows += 1
	curr    += (dataSize * bands * samples) 

hicoFile.close(); 

# results in a file half the size because 'I' expects a 
# 32-bit int. Pillow does not support 16-bit unsigned ints.  
image = Image.frombytes('I', (250, 1000), bytes(stream))
image.show()
