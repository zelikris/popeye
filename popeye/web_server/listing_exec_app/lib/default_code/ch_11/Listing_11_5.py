import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

# Imports
from math import pi
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.pyplot import savefig
from mpl_toolkits.mplot3d.axes3d import Axes3D

from lib.plot import *
from lib.vector_manipulation import *
from objects.vector import *
# Endports

# Can make background white
#plt.gca().patch.set_facecolor('white')
#ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
#ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
#ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))

# Listing 11.04 Simple 3-D line plots
# Begin

subplot(1, 1, 1, projection='3d')
x = vector(0, 0.1, 3*pi)
y1 = plt.np.zeros(len(x))
z1 = sin(x)
z2 = sin(2*x)
z3 = sin(3*x)
y3 = plt.np.ones(len(x))
y2 = y3/2
plot(x, y1, z1, 'r')
plot(x, y2, z2, 'b')
plot(x, y3, z3, 'g')
setlabels('x-axis', 'y-axis', 'z-axis')
setview(30, -120)

# End
