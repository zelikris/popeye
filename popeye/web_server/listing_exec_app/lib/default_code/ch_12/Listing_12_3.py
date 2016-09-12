import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
import matplotlib.patches as patches

# Imports
from matplotlib.path import Path
from lib.anim import *
from lib.plot import *
from lib.librarywrappers import *
# Endports

# Begin
subplot(1, 1, 1)
th = 0
pos = []
scale = []
rate = []  
nst = 20  

def triangle(up, th, pt, sc):
    verts = nparray(((-.5, -.289), (.5, -.289), (0, .577), (-.5, -.289)))
    verts = nptranspose(verts)
    
    codes = [pathmoveto(),
             pathlineto(),
             pathlineto(),
             pathclosepoly(),
    ]
    
    A = sc * nparray(((cosNP(th), -sinNP(th)), (sinNP(th), cosNP(th))))
    thePts = npdot(A, verts)
    thePts = nptranspose(thePts)
    
    thePts[:, 1] *= up
    thePts[:, 0] += pt[0]
    thePts[:, 1] += pt[1]
    path = Path(thePts, codes)

    patch = pathpatch(patches, path, 'orange', 1)
    addpatch(patch)
    
    
def star(pt, sc, v, th):
    triangle(1, v*th, pt, sc)
    plthold(True)
    triangle(-1, v*th, pt, sc)
    pltshow()

def init_sky():    
    pltaxis([-.5, 10.5, -.5, 10.5])
    for ndx in range(0, nst):
        pos.append(rand(1,2)*10)
        scale.append(rand(1,1) * .9 + .1)
        rate.append(rand(1,1) * .5 + 1)
    
def update_sky(i):
    global th   
    
    clearplot()
    for str in range(0, nst):
        star(pos[str][0],
        scale[str][0][0], 
        th, 
        rate[str][0][0])
    th = npmod(th + .1, 20*nppi())

anim = animate(getcurrentfigure(), update_sky, init_sky)
# End
