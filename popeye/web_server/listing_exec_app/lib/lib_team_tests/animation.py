import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

from matplotlib.colors import LightSource
from matplotlib.pyplot import axis, cm
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib import use
use('Agg')

from lib.plot import *
from lib.vector_manipulation import *

from matplotlib.backends.backend_pdf import PdfPages

# Listing 11.10 Creating a subplot
# Begin

subplot(111, projection='3d')

facets = 120
length = 2
radius = 1
thr = np.linspace(0, 2*np.pi, facets)   
xr = [0, length]
[xx, tth] = np.meshgrid(xr, thr)
yy = radius * np.cos(tth)
zz = radius * np.sin(tth)

axis('off')
ls = LightSource(60, 45)
#setview(64, 55)
rgb = ls.shade(zz, cmap=cm.bone)
meshplot(xx, yy, zz, rstride=1, cstride=1, facecolors=rgb,
         linewidth=0, antialiased=False, shade=False)

def animate(i):
    setview(10, (i*2))  
    
ani = animation.FuncAnimation(plt.gcf(), animate, blit=False)
ani.save('3danimtest.mp4', fps=20)

#ani.save('test.jpeg', writer='imagemagick_file')
os.system('ffmpeg -i 3danimtest.mp4 -r 20 -pix_fmt rgb24 final.gif')
os.system('del 3danimtest.mp4') # CLI dependent

