import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

# Imports
from math import pi
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.pyplot import axis, cm
from mpl_toolkits.mplot3d.axes3d import Axes3D
from lib.librarywrappers import *

from lib.plot import *
from lib.vector_manipulation import *
# Endports

# Listing 11.10 Creating a subplot
# Begin

subplot(1, 1, 1, projection='3d')
setaspect('equal')

facets = 120
length = 2
radius = 1
thr = linspace(0, 2*pi, facets)
xr = [0, length]
[xx, tth] = meshgrid(xr, thr)
yy = radius * cosNP(tth)
zz = radius * sinNP(tth)
setview(64, 55)
axis('off')
rgb = shade(60,45,zz, cmap=cm.bone)
meshplot(xx, yy, zz, rstride=1, cstride=1, facecolors=rgb,
         linewidth=0, antialiased=False, shade=False)
         
# End
