import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.path import Path
import matplotlib.patches as patches

fig = plt.figure()
ax = fig.add_subplot(111)
th = 0
pos = []
scale = []
rate = []  
nst = 20  

def triangle( up, th, pt, sc ):
    verts = np.array(((-.5, -.289), (.5, -.289), (0, .577), (-.5, -.289)))
    verts = np.transpose(verts)
    
    codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
    ]
    
    A = sc * np.array(((np.cos(th), -np.sin(th)), (np.sin(th), np.cos(th))))
    thePts = np.dot(A, verts)
    thePts = np.transpose(thePts)
    
    thePts[:, 1] *= up
    thePts[:, 0] += pt[0]
    thePts[:, 1] += pt[1]
    path = Path(thePts, codes)
    
    patch = patches.PathPatch(path, facecolor='orange', lw=1)
    ax.add_patch(patch)
    
    
def star(pt, sc, v, th):
    triangle(1, v*th, pt, sc)
    plt.hold(True)
    triangle(-1, v*th, pt, sc)
    plt.show()

def init_sky():
    global nst
    th = 0
    plt.axis([-.5, 10.5, -.5, 10.5])
    for ndx in range(0, nst):
        pos.append(np.random.rand(1,2)*10)
        scale.append(np.random.rand(1,1) * .9 + .1)
        rate.append(np.random.rand(1,1) * 3 + 1)    
    
def update_sky(i):
    global nst
    global th
    global ax
    
    ax.clear()
    for str in range(0, nst):
        star(pos[str][0],
        scale[str][0][0], 
        th, 
        rate[str][0][0])
    th = np.mod(th + .1, 20*np.pi);
      
plt.axis([-.9, 10.5, -.9, 10.5])
line_ani = animation.FuncAnimation(plt.gcf(), update_sky, 25, init_func=init_sky, interval=50, blit=False)