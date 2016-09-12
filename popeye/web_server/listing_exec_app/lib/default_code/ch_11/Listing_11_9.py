import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

# Imports
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.pyplot import title
from mpl_toolkits.mplot3d.axes3d import Axes3D
from lib.librarywrappers import *
from lib.plot import *
# Endports

# Listing 11.9 Creating a subplot
# Begin

subplot(1, 1, 1, projection='3d')
x = arange(-3, 4, 1)
y = x
xx, yy = meshgrid(x, y)
zz = xx*xx + yy*yy
meshplot(xx, yy, zz, rstride=1, cstride=1, color='w', linewidth=0.5,
         shade=False, edgecolors='r')
title('z = x^2 + y^2')
setlabels('x', 'y', 'z')

# End
