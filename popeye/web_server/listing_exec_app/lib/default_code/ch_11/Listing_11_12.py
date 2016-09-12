import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

# Imports
from math import pi
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.colors import LightSource
from matplotlib.pyplot import axis, cm
from mpl_toolkits.mplot3d.axes3d import Axes3D
from lib.librarywrappers import *

from lib.plot import *
from lib.vector_manipulation import *
# Endports

# Listing 11.12 Creating a subplot
# Begin

subplot(1, 1, 1, projection='3d')
setaspect('equal')
facets = 120
radius = 1
thr = linspace(0, 2*pi, facets)
phir = linspace(0, pi, facets)
th, phi = meshgrid(thr, phir)
x = radius * cosNP(phi)
y = radius * sinNP(phi) * cosNP(th)
z = radius * sinNP(phi) * sinNP(th)

axis('off')
rgb = shade(240, 45,z, cmap=cm.copper)
meshplot(x, y, z, rstride=1, cstride=1, facecolors=rgb,
         linewidth=0, antialiased=False, shade=False)
         
# End
