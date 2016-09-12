import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from matplotlib.colors import LightSource
from matplotlib.pyplot import axis, cm
from mpl_toolkits.mplot3d.axes3d import Axes3D

from lib.plot import *
from lib.vector_manipulation import *
from objects.vector import vector

def listing_02():
    #    % Listing 03.02 Script to solve vector problems
    PA = vector([0, 1, 1])
    print("PA = " + str(PA))
    PB = vector([1, 1, 0])
    print("PB = " + str(PB))
    P = vector([2, 1, 1])
    print("P = " + str(P))
    M = vector([4, 0, 1])
    print("M = " + str(M))
    #% find the resultant of PA and PB
    PC = PA + PB
    print("PC = " + str(PC))
    #% find the unit vector in the direction of PC
    #mag = sqrt(sum(PC.^2))
    mag = vector.magintude(PC)
    print("mag = " + str(mag))
    #unit_vector = PC/mag
    unit_vector = PC/mag
    print("unit_vector = " + str(unit_vector))
    #% find the moment of the force PC about M
    #% this is the cross product of MP and PC
    MP = P - M
    moment = vector.cross( MP, PC )
    print("moment = " + str(moment))
    return moment