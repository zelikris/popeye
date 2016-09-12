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

def Listing_01(x):
# Listing 04.01 if statement example
    print('x = ' + str(x))
    if x == 7:
        state = "Weekend"
    elif x == 1:
        state = "Weekend"
    else:
        state = "Weekday"
    print('state = ' + state)
    return state
    
def Listing_02(grade):
# Listing 04.02 Script with if statements
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
    
def Listing_03(A):
#  Listing 04.03 The if statement with a logical vector
    if all(A):
        print('did not execute')
    if any(A):
        print('any (default) will execute')
    if A:
        print('any (default) will execute')
    A[2] = True
    if A:
        print('will now execute')
    return A

def Listing_04(month, year):
#  Listing 04.04 Example of a switch statement
    for case in switch(month):
       if case(9, 4, 6, 11):
       # Sept, Apr, June, Nov
           days = 30
           break
       if case(2): # Feb
            leapYear = 0
            if year % 4 == 0:
                leapYear = 1
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
    return days

def Listing_05(array):
    if (len(array) > 0):
        theMax = array[0]
        for x in array:
            if x > theMax:
                theMax = x
        return theMax
    else:
        return None
        
def Listing_06(array):
    theMax = array[0]
    theIndex = 0
    for index in np.arange(0, len(array)):
        x = array[index]
        if x > theMax:
            theMax = x
            theIndex = index
    return theIndex    
        
def Listing_07(A):
# Listing 04.07 while statement example
# Testing with a set of hardcoded example for testing purposes
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
        print('the max value in A is ' + str(theMax) + ' at ' + str(theIndex));
    return theIndex
                
def Listing_08(R):
# Listing 04.08 Loop-and-a-half example
    if R > 0:
        area = math.pi * R**2;
        circum = 2 * math.pi * R;
        #areaString = "%.2f" % area
        #circumString = "%.2f" % circumString
        returnString = 'radius = ' + str(R) + '; area = ' + str("%.2f" % area) + '; circum = ' + str("%.2f" % circum)
        print(returnString)
    return returnString

def Listing_09(H, r, h):
# Listing 04.09 Script to compute liquid levels
    print('Height %0.2f; radius %0.2f' %(H, r))
    if h < r:
        v = (0.3333333) * math.pi * h**2 * (3 * r - h);
    elif h < (H-r):
        v = (0.6666666)*math.pi * r**3 + math.pi*r**2*(h-r);
    elif h <= H:
        v = (1.3333333)*math.pi*r**3 + math.pi*r**2*(H-2*r) - (1/3)*math.pi*(H-h)**2*(3*r-H+h);
    else:
        print('liquid level too high')
        return 'liquid level too high'
    vString = "%.2f" % v
    returnString09 = 'rad ' + str("%.2f" % r) + ' ht ' + str("%.2f" % H) + ' level ' + str("%.2f" % h) + ' vol ' + vString
    print('rad ' + str("%.2f" % r) + ' ht ' + str("%.2f" % H) + ' level ' + str("%.2f" % h) + ' vol ' + vString)
    return returnString09
    
#print("\nListing_01\n")
#A = Listing_01();
#print("\nListing_02\n")
#A = Listing_02();
#print("\nListing_03\n")
#A = Listing_03();
#print("\nListing_04\n")
#A = Listing_04();
#print("\nListing_05\n")
#A = Listing_05();
#print("\nListing_06\n")
#A = Listing_06();
#print("\nListing_07\n")
#A = Listing_07();
#print("\nListing_08\n")
#A = Listing_08();
#print("\nListing_09\n")
#A = Listing_09();
