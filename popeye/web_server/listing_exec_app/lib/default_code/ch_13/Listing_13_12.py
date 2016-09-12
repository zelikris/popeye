import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

# Imports
import matplotlib as mpl
from matplotlib._png import read_png
from matplotlib.cbook import get_sample_data
from matplotlib.pyplot import axis
from mpl_toolkits.mplot3d.axes3d import Axes3D
from lib.librarywrappers import *
from lib.plot import *
from lib.vector_manipulation import *
from lib.image_manipulation import *
from math import pi
# Endports

mpl.rcParams['examples.directory'] = '.'

# Listing 13.12
# Begin

# Get image data
input_path = 'input_images/'
fn = get_sample_data(input_path + 'map.png')
img = read_png(fn)

subplot(1, 1, 1, projection='3d')
setaspect('equal')
facets = shape(img, 0)
radius = 1000
thr = linspace(0, 2*pi, facets)
phir = linspace(0, pi, facets)
th, phi = meshgrid(thr, phir)
x = radius * cosNP(phi)
y = radius * sinNP(phi) * cosNP(th)
z = radius * sinNP(phi) * sinNP(th)
setview(-90,0);

axis('off')
meshplot(x, y, z, rstride=5, cstride=5, facecolors=img,
         linewidth=0, antialiased=False, shade=False)
         
# End
