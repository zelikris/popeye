import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

# Imports
from matplotlib.colors import LightSource
from matplotlib.pyplot import axis, cm
from mpl_toolkits.mplot3d.axes3d import Axes3D

from lib.plot import *
from lib.vector_manipulation import *
from objects.vector import vector
# Endports

# Begin

A = vector([2, 5, 7, 1, 3, 4])
print("A = " + str(A))
#odds = 1:2:length(A)
odds = np.arange(1, len(A), 2)
print("odds = " + str(odds))
#disp('odd values of A using predefined indices')
#A(odds)
 # Waiting on Library team for this:
A_odd = A[odds]
print("A_odd = " + str(A_odd))
#disp('odd values of A using anonymous indices')
#A(1:2:end)
print("A_anon_odd = " + str(np.arange(1, len(A), 2)))
#disp('put evens into odd values in a new array')
#B(odds) = A(2:2:end)
B = vector([0, 0, 0, 0, 0, 0])
 # Waiting on Library team for this:
B[odds] = A[odds]
print("B = " + str(B))
#disp('set the even values in B to 99')
#B(2:2:end) = 99
B[np.arange(0,len(B),2)] = 99
print("B = " + str(B))
#disp('find the small values in A')
small = A < 4
#disp('add 10 to the small values')
A[small] = A[small] + 10
print("A = " + str(A))
#disp('this can be done in one ugly operation')
A[A < 10] = A[A < 10] + 10
print("A = " + str(A))
print B

# End
