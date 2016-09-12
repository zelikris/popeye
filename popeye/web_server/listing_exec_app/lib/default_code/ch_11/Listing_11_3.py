import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

# Imports
from math import pi
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.pyplot import axis, grid, xlim

from lib.plot import *
from lib.vector_manipulation import *
from objects.vector import vector
# Endports

# Listing 11.03 Parametric plots
# Begin

z = [None] * 40
w = [None] * 40
th = vector(0, 2*pi/40, 2*pi)
r = 1.1
g = .1
cx = sqrt(r**2 - g**2) - 1
cy = g
x = r*cos(th) + cx
y = r*sin(th) + cy
plot(x, y, 'r')
axis('equal')
plt.hold('true')
grid()
for i in range(0, 40):
    z[i] = complex(x[i], y[i])
    w[i] = z[i] + 1/z[i]
plot(real(w), imag(w), 'k')
xlim(xmax=2.1)

# End
