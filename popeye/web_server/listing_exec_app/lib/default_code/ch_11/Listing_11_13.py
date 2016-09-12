import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

# Imports
from math import pi
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.colors import LightSource
from matplotlib.pyplot import cm, title
from mpl_toolkits.mplot3d.axes3d import Axes3D
from lib.librarywrappers import *

from lib.plot import *
from lib.vector_manipulation import *
# Endports

# Listing 11.13 Creating a subplot
# Begin

facets = 100
u = linspace(0, 5, facets)
th = linspace(0, 2*pi, facets)
uu, tth = meshgrid(u, th)

# Rotate about the x-axis
subplot(1, 2, 1, projection='3d')
rr = uu**2
xx = uu
yy = rr * cosNP(tth)
zz = rr * sinNP(tth)
meshplot(xx, yy, zz, rstride=1, cstride=1, cmap=cm.jet, linewidth=0,
         antialiased=False)
setlabels('x', 'y', 'z')
title('u^2 rotated about the x-axis')

# Rotate about the z-axis
subplot(1, 2, 2, projection='3d')
rr = uu
zz = rr**2
xx = rr * cosNP(tth)
yy = rr * sinNP(tth)
meshplot(xx, yy, zz, rstride=1, cstride=1, cmap=cm.jet, linewidth=0,
         antialiased=False)
setlabels('x', 'y', 'z')
title('u^2 rotated about the z-axis')

# End
