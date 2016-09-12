import sys
import os.path
from matplotlib.colors import LightSource
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import matplotlib.pyplot as plt

ax = None
plotted = False


def plot(*args, **kwargs):
    global plotted
    ax = plt.plot(*args, **kwargs)
    plotted = True


def subplot(*args, **kwargs):
    global ax
    global plotted
    ax = plt.subplot(*args, **kwargs)
    plotted = True


def meshplot(x, y, z, *args, **kwargs):
    global ax
    if ax is not None:
        ax.plot_surface(x, y, z, *args, **kwargs)
        plotted = True
    else:
        raise TypeError('you must select a plot first')


def plot3d(*args, **kwargs):
    global ax
    if ax is not None:
        ax.plot3D(*args, **kwargs)
        plotted = True
    else:
        raise TypeError('you must select a plot first')


def isplotted():
    return plotted


def setaspect(aspect):
    global ax
    ax.set_aspect(aspect)


def setlabels(x, y, z):
    global ax
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_zlabel(z)


def setview(myelev, myazim):
    global ax
    ax.view_init(elev=myelev, azim=myazim)


def text(x, y, z, label):
    global ax
    ax.text(x, y, z, label)
    
    
def addpatch(patch):
    global ax
    ax.add_patch(patch)
    
def clearplot():
    global ax
    ax.clear()
    
def shade(azdeg, altdeg, *args, **kwargs):
    ls = LightSource(azdeg, altdeg)
    return ls.shade(*args, **kwargs)
