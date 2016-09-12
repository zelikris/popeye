import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

# Imports
from math import pi
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.pyplot import title

from lib.plot import *
from lib.vector_manipulation import *
from objects.vector import vector
# Endports

# Listing 11.1 Creating a subplot
# Begin

x = vector(0*pi, .05, 2*pi)
subplot(3, 2, 1)
plot(x, sin(x))
title('1 - sin(x)')
subplot(3, 2, 2)
plot(x, cos(x))
title('2 - cos(x)')
subplot(3, 2, 3)
plot(x, tan(x))
title('3 - tan(x)')
subplot(3, 2, 4)
plot(x, x**2)
title('4 - x^2')
subplot(3, 2, 5)
plot(x, plt.np.sqrt(x))
title('5 - sqrt(x)')
subplot(3, 2, 6)
plot(x, plt.np.exp(x))
title('4 - e^x')

# End
