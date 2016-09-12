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