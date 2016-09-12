import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

# Imports
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.pyplot import axis
from mpl_toolkits.mplot3d.axes3d import Axes3D

from lib.plot import *
from lib.vector_manipulation import *
# Endports

# Begin

subplot(1, 1, 1, projection='3d')
setaspect('equal')
axis('off')

# Face 1
x1 = [[0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]
y1 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
z1 = [[0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
# Face 2
x2 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
y2 = [[0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]
z2 = [[0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
# Face 3
x3 = [[0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]
y3 = [[0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
z3 = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
# Face 4
x4 = [[0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]
y4 = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
z4 = [[0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
# Face 5
x5 = [[0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
y5 = [[0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]
z5 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# Face 6
x6 = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
y6 = [[0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]
z6 = [[0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]

meshplot(x1, y1, z1)
meshplot(x2, y2, z2)
meshplot(x3, y3, z3)
meshplot(x4, y4, z4)
meshplot(x5, y5, z5)
meshplot(x6, y6, z6)

# End
