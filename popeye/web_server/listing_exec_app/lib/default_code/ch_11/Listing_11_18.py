import sys
import os.path

import matplotlib.pyplot as plt
from matplotlib import cm

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

# Imports
from plot import *
from vector_manipulation import *
# Endoports

# Begin
raw = np.loadtxt('atlanta.txt', delimiter='\t')
streets = raw[:,2:7]
(rows, cols) = streets.shape
colors = 'rgbkcmo'
subplot(1, 1, 1)
for temp in xrange(0, rows):
    x = streets[temp, [0, 2]] / 1000000
    y = streets[temp, [1, 3]] / 1000000
    col = streets[temp, 4]
    if not 0 <= col <= 5:
        col = 6
    plot(x, y, colors[int(col)])

tt = np.loadtxt('ttimes.txt', delimiter='\t')
(rows, cols) = tt.shape
xc = []
yc = []
zc = []
for temp in xrange(0, rows):
    r = tt[temp, 0]
    c = tt[temp, 1]
    if (len(xc) < r):
        xc.append([])
    if (len(xc[int(r - 1)]) < c):
        xc[int(r - 1)].append(tt[temp, 3] / 1000000)
    if (len(yc) < r):
        yc.append([])
    if (len(yc[int(r - 1)]) < c):
        yc[int(r - 1)].append(tt[temp, 4] / 1000000)
    if (len(zc) < r):
        zc.append([])
    if (len(zc[int(r - 1)]) < c):
        zc[int(r - 1)].append(tt[temp, 5])   

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xc, yc, zc, rstride=1, cstride=1, linewidth=0, antialiased=False, shade=False, cmap=cm.bwr)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_zlabel('Travel Time (min)')
plt.show()
#meshplot(xc, yc, zc,  rstride=1, cstride=1, linewidth=0, antialiased=False, shade=False)

# End