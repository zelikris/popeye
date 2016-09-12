def Listing_05():
# Listing 04.05 Example of a for statement
    A = [6, 12, 6, 91, 13, 6] # initial vector
    print('A = ' + str(A))
    theMax = A[0]; # set initial max value
    for x in A: # iterate through A
        if x > theMax: # test each element
            theMax = x
    print('max(A) is ' + str(theMax))    