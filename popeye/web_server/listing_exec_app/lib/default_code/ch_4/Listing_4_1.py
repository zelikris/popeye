import numpy as np

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