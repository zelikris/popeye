import numpy as np
#Listing 04.07 while statement example
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
    print('the max value in A is ' + str(theMax) + ' at ' + str(theIndex));