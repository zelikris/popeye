import numpy as np
import math

def listing_01():
#% Listing 03.01 Vector indexing script
#A = [2 5 7 1 3 4]
    A = np.array([2, 5, 7, 1, 3, 4])
    print("A = " + str(A))
    #odds = 1:2:length(A)
    odds = np.arange(1, len(A), 2)
    print("odds = " + str(odds))
    #disp('odd values of A using predefined indices')
    #A(odds)
    A_odd = A[odds]
    print("A_odd = " + str(A_odd))
    #disp('odd values of A using anonymous indices')
    #A(1:2:end)
    print("A_anon_odd = " + str(np.arange(1, len(A), 2)))
    #disp('put evens into odd values in a new array')
    #B(odds) = A(2:2:end)
    B = np.zeros(6,dtype=int)
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
    return B
    
def listing_02():
    #    % Listing 03.02 Script to solve vector problems
    PA = np.array([0, 1, 1])
    print("PA = " + str(PA))
    PB = np.array([1, 1, 0])
    print("PB = " + str(PB))
    P = np.array([2, 1, 1])
    print("P = " + str(P))
    M = np.array([4, 0, 1])
    print("M = " + str(M))
    #% find the resultant of PA and PB
    PC = PA + PB
    print("PC = " + str(PC))
    #% find the unit vector in the direction of PC
    #mag = sqrt(sum(PC.^2))
    mag = math.sqrt(sum(PC**2))
    print("mag = " + str(mag))
    #unit_vector = PC/mag
    unit_vector = PC/mag
    print("unit_vector = " + str(unit_vector))
    #% find the moment of the force PC about M
    #% this is the cross product of MP and PC
    MP = P - M
    moment = np.cross( MP, PC )
    print("moment = " + str(moment))

def listing_03():
    #% Listing 03.03 Array manipulation script
    A = np.array([[2, 5, 7, 3], [1, 3, 4, 2]])
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
    B = np.zeros(8).reshape(2,4)
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
    
def listing_04():
    # Listing 03.04 Script to compute total soil
    # soil depth data for each square produced by the survey
    depth = np.array([[8,8,9,8,8,8,8,8,7,8,7,7,7,7,8,8,8,7],
        [8,8,8,8,8,8,8,7,7,7,7,7,8,7,8,8,8,7],
        [8,8,8,8,7,7,8,7,8,8,8,8,8,7,8,8,8,8],
        [7,7,7,8,7,8,8,8,8,8,8,8,7,6,7,7,7,7],
        [8,8,8,8,8,8,8,8,7,7,7,7,7,6,6,7,7,8],
        [8,7,7,8,7,7,8,7,7,7,7,7,7,7,7,7,7,8],
        [9,8,8,9,8,7,8,7,7,7,7,7,6,7,6,7,7,8],
        [8,8,8,9,9,8,8,8,7,6,6,6,6,7,7,8,7,8],
        [9,8,8,7,7,7,7,7,7,6,6,7,7,7,8,8,7,8],
        [9,8,8,7,7,7,6,7,7,6,6,8,8,8,9,9,7,8],
        [9,9,8,8,8,8,7,7,7,7,7,8,8,9,9,9,8,8],
        [9,8,8,7,7,8,7,7,7,7,8,8,9,9,9,8,7,8]]);
    # estimated proportion of each square that should be excavated
    area = np.array([[1,1,1,1,1,1,1,1,1,1,.3,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,1,.7,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,1,1,.8,.4,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,.8,.3,0,0,0],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,.7,.2,0,0],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,.6,0,0],
        [0,0,0,.7,1,1,1,1,1,1,1,1,1,1,1,.8,0,0],
        [0,0,0,.7,1,1,1,1,1,1,1,1,1,1,1,.7,0,0],
        [0,0,0,.4,1,1,1,1,1,1,1,1,1,1,1,.6,0,0],
        [0,0,0,.1,.8,1,1,1,1,1,1,1,1,1,1,1,.4,0],
        [0,0,0,0,.2,.7,1,1,1,1,1,1,1,1,1,1,.9,.1],
        [0,0,0,0,0,0,.4,.8,.9,1,1,1,1,1,1,1,1,.6]]);
#    depth = np.array([[8,8,9],
#         [8,8,8]]);
    print('depth = ' + str(depth))
    # estimated proportion of each square that should be excavated
#    area = np.array([[1,1,1],
#         [1,1,1]]);
    print('area = ' + str(area))
    square_volume = depth * area;
    print('square_volume = ' + str(square_volume))
    total_soil = np.sum(np.sum(square_volume))
    print('total_soil = ' + str(total_soil))


def junk():
    # from the Python Tutorial page 
    a = np.arange(12).reshape(3,4)
    print("a = " + str(a))
    i = np.array( [ [0,1],  [1,2] ] )
    print("i = " + str(i))
    j = np.array( [ [2,1],  [3,3] ] )
    print("j = " + str(j))
    it = a[i,j]        # i and j must have equal shape
    print("a[i,j] = " + str(it))
    it = a[i,2]        # i and j must have equal shape
    print("a[i,2] = " + str(it))
    it = a[:,j]        # i and j must have equal shape
    print("a[:,j] = " + str(it))
    x = np.arange(10);
    x.shape = (2,5)
    print("x = " + str(x))  
    y = np.arange(35).reshape(5,7)
    print("y = " + str(y))  
    print("y[1:5:2,::3] = " + str(y[1:5:2,::3]))  
    print("y[np.array([0,2,4]), np.array([0,1,2])] = " 
    + str(y[np.array([0,2,4]), np.array([0,1,2])]))  
    print("y[np.array([0,2,4]), 1] = " + str(y[np.array([0,2,4]), 1]))  
    print("y[np.array([0,2,4])] = " + str(y[np.array([0,2,4])]))  
    print("y[y>20] = " + str(y[y>20]))  
    print("y[(y>25)|(y<5)] = " + str(y[(y>20) | (y<5)]))  
    print("y[np.array([0,2,4]),1:3] = " + str(y[np.array([0,2,4]),1:3])) 
    even = a%2 == 0
    print("a even is " + str(even))
    wh = np.where(even)
    print("where is a even " + str(wh))
    ae = a[wh]
    print("a even = " + str(ae))
    
    
#print("\njunk")
#A = junk()
#print("\nListing_03_01")
#B = listing_01()
#print("\nListing_03_02")
#C = listing_02()
#print("\nListing_03_03")
#A = listing_03()
print("\nListing_03_04")
A = listing_04()


