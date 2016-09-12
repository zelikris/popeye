import numpy as np

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