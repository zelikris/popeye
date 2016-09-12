import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

# Imports
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.pyplot import legend, title, xlabel, ylabel

from lib.plot import *
from lib.vector_manipulation import *
# Endports

# Listing 11.2 Simple 2-D plots
# Begin

x = vector(-1.5, 0.103, 1.5)
clr = 'rgbk'
for pwr in range(1,5):
    plot(x, x**pwr, color=clr[pwr-1], label=str(pwr))
xlabel('x')
ylabel('x^N')
title('Powers of x')
legend(['1', '2', '3', '4'], loc='lower right')

# End
