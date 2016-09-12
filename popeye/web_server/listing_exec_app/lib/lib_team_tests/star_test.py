import numpy as np
import numpy.matlib as ml
import matplotlib.pyplot as plt
from matplotlib import animation

def triangle( up, th, pt, sc ):
    print 'triangle'
    pts = [[-.5,    .5,    0,   -.5],
           [-.289, -.289, .577, -.289]]
           
    A = sc * np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]]) 
#    np.dot(sc, [[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
#    print A
    thePts = np.dot(A, pts)
    
#    print thePts[0,:]
#    print pt
    plt.plot(thePts[0,:] + ml.repmat(pt[0],1,4), up*thePts[1,:] + ml.repmat(pt[1],1,4))
#    plt.plot(2, 2, 'y', 5, 5, 'r')    
    #fill( thePts(1,:) + pt(1), up*thePts(2,:) + pt(2), 1)

def star(pt, sc, v, th):
    triangle(1, v*th, pt, sc)
    plt.hold(True)
    triangle(-1, v*th, pt, sc)
    plt.show()
    
nst = 20
#th = 0
pos = []
scale = []
rate = []

def init_sky():
    nst = 20
    th = 0
    plt.axis([-.5, 10.5, -.5, 10.5])
    for ndx in range(0, nst):
        pos.append(np.random.rand(1,2)*10)
        scale.append(np.random.rand(1,1) * .9 + .1)
        rate.append(np.random.rand(1,1) * 3 + 1)



def update_sky(i):
    print i
    global nst
    global th
    x = np.arange(0, 5, 0.1)
    y = np.sin(x)
    plt.plot(x, y)
    
    for str in range(0, nst):
        star(pos[str][0],
        scale[str][0][0], 
        th, 
        rate[str][0][0])
        
#    axis equal 
    
#    axis([-.5 10.5 -.5 10.5])
#    axis off
    plt.hold(False)
    th = np.mod(th + .1, 20*np.pi);

#    pause(0.1)
line_ani = animation.FuncAnimation(plt.gcf(), update_sky, 25, init_func=init_sky, interval=50, blit=False)
plt.show()