import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

# Imports
from math import pi
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.colors import LightSource
from matplotlib.pyplot import axis, cm, title
from mpl_toolkits.mplot3d.axes3d import Axes3D
from lib.librarywrappers import *

from lib.plot import *
from lib.vector_manipulation import *
# Endports

# Begin

u = [0, 0, 3, 3, 1.75, 1.75, 2, 2, 1.75, 1.75, 3, 4, 5.25, 5.25, 5, 5, 5.25,
     5.25, 3, 3, 6, 6]
v = [0, 0.5, 0.5, 0.502, 0.502, 0.55, 0.55, 1.75, 1.75, 2.5, 2.5, 1.5, 1.5,
     1.4, 1.4, 0.55, 0.55, 0.502, 0.502, 0.5, 0.5, 0]
subplot(1, 2, 1)
plot(u, v, 'k')
axis('off')
title('2-D profile')
facets = 200
subplot(1, 2, 2, projection='3d')
xx, tth = meshgrid(u, np.linspace(0, 2*pi, facets))
rr = meshgrid(v, np.arange(1, facets + 1, 1))
yy = rr * cosNP(tth)
zz = rr * sinNP(tth)
title('rotated object')
axis('off')
rgb = shade(60, 45,zz[0], cmap=cm.bone)
meshplot(xx, yy[0], zz[0], rstride=1, cstride=1, facecolors=rgb,
         linewidth=0, antialiased=False, shade=False)
         
# End
