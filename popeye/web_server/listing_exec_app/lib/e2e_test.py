# -*- coding: utf-8 -*-
"""
Created on Wed Sep 09 15:06:58 2015

@author: Mitch Webster
"""
#not visisible to programmer

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from matplotlib.pyplot import *
#need for 3d 
from mpl_toolkits.mplot3d.axes3d import Axes3D
from objects.vector import vector

from matplotlib.backends.backend_pdf import PdfPages
import datetime
import time
import numpy as np
import libglobals
from plot import *

#visisible to programmer

vec_x = vector(31.1, 78, -1.47,55,28,91)
vec_y = vector(2.1, 22.9, -36,22,10,37)
vec_z = vector(100.1, 1.9, -3,22,50,37)

subplot(2,2,1)
hold(False)
plot(vec_x, vec_y, vec_y, vec_z)
plot(vec_y, vec_z)
title("Hold off example")
xlabel("Some X label")
ylabel("Some Y label")

subplot(2,2,3)
hold(True)
plot(vec_x, vec_y, vec_y, vec_z)
plot(vec_z, vec_z)
title("Hold on example w/ multiplot")

subplot(2,2,2, projection='3d')
plot(vec_z,vec_x, vec_y)
plot(vec_x, vec_y, vec_z)
title("3d plot")
xlabel("test xlabel")
ylabel("test ylabel")

subplot(2,2,4, projection='3d')
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
xlabel("test xlabel 2")
ylabel("test ylabel 2")
meshplot(x, y, z, rstride=5, cstride=5, color='y')

#not visible to programmer
tight_layout(pad=0.4, w_pad=0.5, h_pad=2.0)
save_path = '../pdfs/'+ libglobals.title_general + datetime.datetime.fromtimestamp(time.time()).strftime('_%Y-%m-%d_%H-%M-%S');
#possibly handle concurrent requests
#while (os.path.exists(save_path+'.pdf')):'
print 'Fileplotted ?',
print isplotted()
save_path += '.pdf'
pp = PdfPages(save_path)
pp.savefig(gcf())
pp.close()
