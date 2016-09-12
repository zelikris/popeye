import math
# Listing 04.08 Loop-and-a-half example
R = 1;
while R > 0:
    R = input('Enter a radius: ')
    if R > 0:
        area = math.pi * R**2;
        circum = 2 * math.pi * R;
        returnString = 'radius = ' + str(R) + '; area = ' + str(area) + '; circum = ' + str(circum)
        print(returnString1);