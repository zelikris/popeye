import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from matplotlib.colors import LightSource
from matplotlib.pyplot import axis, cm
from mpl_toolkits.mplot3d.axes3d import Axes3D

from lib.plot import *
from lib.vector_manipulation import *
from objects.vector import vector

def listing_03():
    #% Listing 03.03 Array manipulation script
    A = np.array([vector([2, 5, 7, 3]), vector([1, 3, 4, 2])])
    print("A = " + str(A))
    #[rows, cols] = size(A)
    rows = A.shape[0]
    cols = A.shape[1]
    print("rows = " + str(rows) + "; cols = " + str(cols))
    print("odd columns of A using explicit indices")
    odds = np.arange(1,cols,2)
    print("odds = " + str(odds))
    oddc = A[:, odds]
    print("odd columns of A using explicit indices")
    print("odd cols of A = " + str(oddc))
    print("odd columns of A using anonymous indices")
    oddc = A[:, np.arange(1,cols,2)]
    print("anon odd cols of A = " + str(oddc))
    print('put evens into odd values in a new array')
    print('A.shape = ' + str(A.shape))
    #Regression Test fails--waiting on library team
    B = vector([0, 0, 0, 0, 0, 0, 0, 0]).reshape(2,4)
    print("B = " + str(B))
    B[:, odds] = A[:, np.arange(1,cols,2)]
    print("B = " + str(B))
    print('set the even values in B to 99')
    B[:, np.arange(0,cols,2)] = 99
    print("B = " + str(B))
    print('find the small values in A')
    print('A = ' + str(A))
    small = A < 4
    print('small = ' + str(small))
    print('add 10 to the values less than 4')
    A[small] = A[small] + 10
    print('A = ' + str(A))
    print('this can be done in one ugly operation')
    A[A < 6] = A[A < 6] + 10
    small_index = np.where(small)
    print('small_index = ' + str(small_index))
    A[small_index] = A[small_index] + 100
    print('A = ' + str(A))
    return A