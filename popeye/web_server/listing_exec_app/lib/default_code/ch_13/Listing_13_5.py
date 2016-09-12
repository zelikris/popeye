import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

# Imports
from lib.librarywrappers import *

from skimage import filter
from lib.image_manipulation import *
# Endports

# Begin
input_path = 'input_images/'
image = imread(input_path + "C-130.jpg")  # or any NumPy array!
image = rgb2gray(image)
edges = filter.sobel(image)
imshow(edges, cmap='Greys',  interpolation='nearest')
# End
