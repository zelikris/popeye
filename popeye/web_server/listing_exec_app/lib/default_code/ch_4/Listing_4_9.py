import math
# Listing 04.09 Script to compute liquid levels
another_tank = True
while another_tank:
    H = (float)(input('Overall tank height: '))
    r = (float)(input('tank radius: '))
    more_heights = True
    print('Height %0.2f; radius %0.2f' %(H, r))
    while more_heights:
        h = (float)(input('liquid height: '))
        if h < r:
            v = (0.333333)*math.pi*h**2.*(3*r-h)
        elif h < H-r:
            v = (0.666666)*math.pi*r**3 + math.pi*r**2*(h-r)
        elif h <= H:
            v = (1.333333)*math.pi*r**3 + math.pi*r**2*(H-2*r) - (1/3)*math.pi*(H-h)**2*(3*r-H+h)
        else:
            print('liquid level too high')
            continue
        print( '    rad %0.2f ht %0.2f level %0.2f vol %0.2f' % (r, H, h, v))
        more_heights = input('more levels? (True/False)')
    another_tank = input('more tank? (True/False)')