import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

# Imports
from pylab import *
from lib.plot import *
from lib.librarywrappers import *
from lib.anim import *
# Endports 
 
# Begin
 
def quaternion_to_matrix(myx):
    xb, xc, xd = myx
 
    xnormsq = xb*xb + xc*xc + xd*xd
 
    if xnormsq < 1:
        b, c, d = xb, xc, xd
        a = sqrt(1 - xnormsq)
    else:
        b, c, d = -xb / xnormsq, -xc / xnormsq, -xd / xnormsq
        a = -sqrt(1 - 1.0/xnormsq)
 
    return nparray([ [(a*a + b*b - c*c - d*d), (2*b*c - 2*a*d), (2*b*d+2*a*c)   ],
                      [(2*b*c + 2*a*d), (a*a - b*b + c*c - d*d), (2*c*d - 2*a*b)],
                      [(2*b*d - 2*a*c), (2*c*d + 2*a*b), (a*a - b*b - c*c + d*d)]]).T  \
                         / (a*a + b*b + c*c + d*d)
                         

def rotation(ind, Nind):
    return quaternion_to_matrix(0.5*sin(pi*2*ind*Nind** - 1.*array([1, 2, 3])))
 
 
def project(D, vecs):
    return vecs[:, :2] / (vecs[:, [2, 2]] - D)
 
 
vs = reshape(mgrid[-1:2:2, -1:2:2, -1:2:2].T, (8, 3))
 
ed=[(j,k)
    for j in range(8)
    for k in range(j, 8)
    if sum(abs(vs[j] - vs[k])) == 2 ]
 
 
D= -5
fig = figure(1, figsize=(6.4, 4.8))
subplot(1, 1, 1)
Nind=250
 

def update_func(i):
    clearplot()
    rotM = rotation(i, Nind)
    
    # first cube
    vvs=dot(vs, rotM)
    pt = project(D, vvs)
    for j, k in ed:
        plot(pt[[j, k], 0], pt[[j, k], 1], '-r', lw = 3)    
    
    # second cube
    rot2 = rotation((i + 5) * 2, Nind)
    vvs2 = dot(vs, rot2)
    pt2 = project(D, vvs2)
    for j, k in ed:
        plot(pt2[[j, k], 0] + 1, pt2[[j, k], 1], '-r', lw = 3)
 
    axis('equal')
    axis([-0.5, 1.5, -0.4, 0.4])

 
anim = animate(fig, update_func)
# End
