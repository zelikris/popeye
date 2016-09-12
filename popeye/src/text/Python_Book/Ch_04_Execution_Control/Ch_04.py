import numpy as np
import math
# This class provides switch functionality. You only need to look at
# this if you want to know how this works. It only needs to be defined
# once, no need to muck around with its internals.
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

def Listing_01():
# Listing 04.01 if statement example
    x = np.random.randint(8, size=1)
    print('x = ' + str(x))
    if x == 7:
        state = "Weekend"
    elif x == 1:
        state = "Weekend"
    else:
        state = "Weekday"
    print('state = ' + state)
    return state
    
def Listing_02():
# Listing 04.02 Script with if statements
    grade = np.random.randint(40, 101, size=1)
    print('grade = ' + str(grade))
    if grade >= 90:
        letter = 'A'
    elif grade >= 80:
        letter = 'B'
    elif grade >= 70:
        letter = 'C'
    elif grade >= 60:
        letter = 'D'
    else:
        letter = 'F'
    print("grade " + str(grade) + ' gets a grade of ' + letter)
    return letter
    
def Listing_03():
#  Listing 04.03 The if statement with a logical vector
    A = [True, True, False]
    if all(A):
        print('did not execute')
    if any(A):
        print('any (default) will execute')
    if A:
        print('any (default) will execute')
    A[2] = True;
    if A:
        print('will now execute')
    return A

def Listing_04():
#  Listing 04.04 Example of a switch statement
#    month = int(input('month number? '))
    month = np.random.randint(1,13, size=1)
    print('month = ' + str(month))
    for case in switch(month):
       if case(9, 4, 6, 11):
       # Sept, Apr, June, Nov
           days = 30;
           break
       if case(2): # Feb
#            answer = input('is this a leap year? ')
#            leapYear = (len(answer) > 0) and (answer[0] == 'y')
            rn = np.random.randint(2, size=1)
            leapYear = rn%2 == 1;
            if leapYear:
               days = 29;
            else:
               days = 28;
            break
       if case(1, 3, 5, 7, 8, 10, 12):
            # other months
            days = 31;
            break
       if case():
            print('bad month index')
            break
    print('month ' + str(month) + " has " + str(days) + ' days')

def Listing_05():
# Listing 04.05 Example of a for statement
    A = [6, 12, 6, 91, 13, 6] # initial vector
    print('A = ' + str(A))
    theMax = A[0]; # set initial max value
    for x in A: # iterate through A
        if x > theMax: # test each element
            theMax = x;
    print('max(A) is ' + str(theMax));
        
def Listing_06():
# Listing 04.06 for statement using indexing
    A = np.random.randint(100, size=10)
    print('A = ' + str(A))
    theMax = A[0];
    theIndex = 0;
    for index in np.arange(0,len(A)):
        x = A[index];
        if x > theMax:
            theMax = x;
            theIndex = index;
    print('the max value in A is ' + str(theMax) +
                            ' at ' + str(theIndex));
        
def Listing_07():
# Listing 04.07 while statement example
    A = np.random.randint(100, size=10)
    print('A = ' + str(A))
    theMax = A[0];
    theIndex = 0;
    index = 0;
    while index < len(A):
        x = A[index];
        if x > theMax:
           theMax = x;
           theIndex = index;
        index = index + 1;
    print('the max value in A is ' + str(theMax)
                + ' at ' + str(theIndex));
                
def Listing_08():
# Listing 04.08 Loop-and-a-half example
    R = 1;
    while R > 0:
        R = np.random.randint(10, size=1)
        if R > 0:
            area = math.pi * R**2;
            circum = 2 * math.pi * R;
            print('radius = ' + str(R) 
                + 'area = ' + str(area) 
                + '; circum = ' + str(circum));

def Listing_09():
# Listing 04.09 Script to compute liquid levels
    another_tank = True;
    while another_tank:
        H = np.random.rand() * 20;
        r = np.random.rand() * 20;
        more_heights = True;
        print('Height %0.2f; radius %0.2f' %(H, r))
        while more_heights:
            h = np.random.rand() * H;
            if h < r:
                v = (1/3)*math.pi*h**2.*(3*r-h);
            elif h < H-r:
                v = (2/3)*math.pi*r**3 + math.pi*r**2*(h-r);
            elif h <= H:
                v = (4/3)*math.pi*r**3 + math.pi*r**2*(H-2*r) 
                - (1/3)*math.pi*(H-h)**2*(3*r-H+h);
            else:
                print('liquid level too high')
                continue
            print( '    rad %0.2f ht %0.2f level %0.2f vol %0.2f' %
                (r, H, h, v));
            it = np.random.randint(20, size=1);
            more_heights = it > 3;
        it = np.random.randint(20, size=1);
        another_tank = it > 3
    
print("\nListing_01\n")
A = Listing_01();
print("\nListing_02\n")
A = Listing_02();
print("\nListing_03\n")
A = Listing_03();
print("\nListing_04\n")
A = Listing_04();
print("\nListing_05\n")
A = Listing_05();
print("\nListing_06\n")
A = Listing_06();
print("\nListing_07\n")
A = Listing_07();
print("\nListing_08\n")
A = Listing_08();
print("\nListing_09\n")
A = Listing_09();
