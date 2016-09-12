import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
import numpy.matlib as npm
from matplotlib.path import Path
import matplotlib.pyplot as plt

def rand(a, b):
    return np.random.rand(a, b)


def cumsum(val):
    return np.cumsum(val)


def sinNP(theta):
    return np.sin(theta)
    
    
def cosNP(theta):
    return np.cos(theta)
    
    
def arange(start, stop, step):
    return np.arange(start, stop, step)
    
    
def linspace(start, end, num):
    return np.linspace(start, end, num)
    
    
def meshgrid(*xi, **kwargs):
    return np.meshgrid(*xi, **kwargs)
    
    
def sqrt(num):
    return np.sqrt(num)
    
    
def real(num):
    return np.real(num)


def imag(num):
    return np.imag(num)
    
    
def empty(shape, dtype=float, order='C'):
    return np.empty(shape, dtype, order)
    
    
def repmat(a, m, n):
    return npm.repmat(a, m, n)
    
    
def logical_and(x1, x2):
    return np.logical_and(x1, x2)
    
    
def greater(x1, x2):
    return np.greater(x1, x2)


def npcopyto(src, dst):
    return np.copyto(src, dst)


def size(array, dim):
    return array.shape[dim]
    
    
def astype(array, dtype):
    return array.astype(dtype)
    
    
def nparray(object):
    return np.array(object)
    
    
def nptranspose(object):
    return np.transpose(object)
    
    
def npdot(a, b):
    return np.dot(a, b)
    
    
def concatenate(array, axis=0):
    return np.concatenate(array, axis)

    
def pathmoveto():
    return Path.MOVETO


def pathlineto():
    return Path.LINETO

    
def pathclosepoly():
    return Path.CLOSEPOLY
    
    
def pathpatch(patches, path, color, linewidth):
    return patches.PathPatch(path, facecolor=str(color), lw=linewidth)
    
    
def plthold(isHold):
    plt.hold(isHold)
    
    
def pltshow():
    plt.show()
    
    
def pltaxis(axis):
    plt.axis(axis)
    

def npmod(a, b):
    return np.mod(a, b)
    
    
def nppi():
    return np.pi
    
def getcurrentfigure():
    return plt.gcf()