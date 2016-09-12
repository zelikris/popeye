def Listing_06():
# Listing 04.06 for statement using indexing
    A = np.random.randint(100, size=10)
    print('A = ' + str(A))
    theMax = A[0]
    theIndex = 0
    for index in np.arange(0,len(A)):
        x = A[index]
        if x > theMax:
            theMax = x
            theIndex = index
    print('The max value is ' + str(theMax) + ' at index ' + str(theIndex))