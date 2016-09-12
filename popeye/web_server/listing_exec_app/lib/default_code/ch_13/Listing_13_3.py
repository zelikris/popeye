import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

# Imports
from lib.image_manipulation import *
from lib.librarywrappers import *
from lib.plot import *
# Endports

# Listing 13.03 Making a kaleidoscope
# Begin
input_path = 'input_images/'
sb = imread(input_path + 'sqbutter.jpg')
subplot( 1, 2, 1)
image(sb)
cols = size(sb, 1)
mid = cols/2
subplot( 1, 2, 2)
a = concatenate((diagMirror( sb[0:mid-1, 0:mid-1, :], 0 ), \
                        diagMirror( sb[0:mid-1, mid:cols-1, :], 3 )), axis=1)
b = concatenate((diagMirror( sb[mid:cols-1, 0:mid-1, :], 1 ), \
                    diagMirror( sb[mid:cols-1, mid:cols-1, :], 2 )), axis=1)
img = concatenate((a,b), axis=0)
image(img)
# End
