import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

# Imports
from lib.image_manipulation import *
from lib.plot import *
from lib.librarywrappers import *
# Endports

# Listing 13.01 Exploring the sky situation
# Begin
input_path = 'input_images/'
v = imread(input_path + 'Vienna.jpg')
image(v)
row = 400
red = v[row, :, 0]
gr = v[row, :, 1]
bl = v[row, :, 2]
plot(red, 'r')
plot(gr, 'g')
plot(bl, 'b')
# End
