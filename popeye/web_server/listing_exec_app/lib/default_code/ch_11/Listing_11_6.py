import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

# Imports
from math import pi
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.pyplot import title
from mpl_toolkits.mplot3d.axes3d import Axes3D
import random

from lib.plot import *
from lib.vector_manipulation import *
from objects.vector import *
# Endports

# Begin

subplot(1, 2, 1, projection='3d')
theta = vector(0, 0.1, 10*pi)
plot3d(sin(theta), cos(theta), theta)
title('Parametric curve \nbased on angle')
N = 20
dvx = rand(1, N) - 0.5
dvy = rand(1, N) - 0.5
dvz = rand(1, N) - 0.5
x = cumsum(cumsum(dvx))
y = cumsum(cumsum(dvy))
z = cumsum(cumsum(dvz))
subplot(1, 2, 2, projection='3d')
plot3d(x, y, z)
title('All 3 axes varying \nwith parameter t')
text(0, 0, 0, 'start')
text(x[N-1], y[N-1], z[N-1], 'end')

# End
