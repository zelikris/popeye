import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from matplotlib.colors import LightSource
from matplotlib.pyplot import axis, cm
from mpl_toolkits.mplot3d.axes3d import Axes3D

from lib.plot import *
from lib.vector_manipulation import *
from objects.vector import vector

def listing_04():
    # Listing 03.04 Script to compute total soil
    # soil depth data for each square produced by the survey
    depth = np.array([
        vector([8,8,9,8,8,8,8,8,7,8,7,7,7,7,8,8,8,7]),
        vector([8,8,8,8,8,8,8,7,7,7,7,7,8,7,8,8,8,7]),
        vector([8,8,8,8,7,7,8,7,8,8,8,8,8,7,8,8,8,8]),
        vector([7,7,7,8,7,8,8,8,8,8,8,8,7,6,7,7,7,7]),
        vector([8,8,8,8,8,8,8,8,7,7,7,7,7,6,6,7,7,8]),
        vector([8,7,7,8,7,7,8,7,7,7,7,7,7,7,7,7,7,8]),
        vector([9,8,8,9,8,7,8,7,7,7,7,7,6,7,6,7,7,8]),
        vector([8,8,8,9,9,8,8,8,7,6,6,6,6,7,7,8,7,8]),
        vector([9,8,8,7,7,7,7,7,7,6,6,7,7,7,8,8,7,8]),
        vector([9,8,8,7,7,7,6,7,7,6,6,8,8,8,9,9,7,8]),
        vector([9,9,8,8,8,8,7,7,7,7,7,8,8,9,9,9,8,8]),
        vector([9,8,8,7,7,8,7,7,7,7,8,8,9,9,9,8,7,8])
            ]);
    # estimated proportion of each square that should be excavated
    area = np.array([
        vector([1,1,1,1,1,1,1,1,1,1,.3,0,0,0,0,0,0,0]),
        vector([1,1,1,1,1,1,1,1,1,1,.7,0,0,0,0,0,0,0]),
        vector([1,1,1,1,1,1,1,1,1,1,1,.8,.4,0,0,0,0,0]),
        vector([1,1,1,1,1,1,1,1,1,1,1,1,1,.8,.3,0,0,0]),
        vector([1,1,1,1,1,1,1,1,1,1,1,1,1,1,.7,.2,0,0]),
        vector([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,.6,0,0]),
        vector([0,0,0,.7,1,1,1,1,1,1,1,1,1,1,1,.8,0,0]),
        vector([0,0,0,.7,1,1,1,1,1,1,1,1,1,1,1,.7,0,0]),
        vector([0,0,0,.4,1,1,1,1,1,1,1,1,1,1,1,.6,0,0]),
        vector([0,0,0,.1,.8,1,1,1,1,1,1,1,1,1,1,1,.4,0]),
        vector([0,0,0,0,.2,.7,1,1,1,1,1,1,1,1,1,1,.9,.1]),
        vector([0,0,0,0,0,0,.4,.8,.9,1,1,1,1,1,1,1,1,.6]),
        ]);
#    depth = np.array([[8,8,9],
#         [8,8,8]]);
    print('depth = ' + str(depth))
    # estimated proportion of each square that should be excavated
#    area = np.array([[1,1,1],
#         [1,1,1]]);
    print('area = ' + str(area))
    square_volume = depth * area;
    print('square_volume = ' + str(square_volume))
    # Waiting on the library team to fix this:
    total_soil = np.sum(np.sum(square_volume))
    print('total_soil = ' + str(total_soil))