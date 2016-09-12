import numpy as np
import math

def cylinder(height, radius):
# Listing 5.2 - cylinder function returning area and volume 
    base = math.pi * radius**2
    volume = base * height
    area = 2*base + 2*math.pi*radius*height
    return (area, volume, base)


def Listing_03():
# Listing 05.03 Volume and area of a disk
    h = np.arange(1,6) # set a range of disk thicknesses
    R = 25;
    r = 3;
    Area, Vol, Junk = cylinder(h, R) # dimensions of large disk
    for ndx in np.arange(0, len(h)):
        print('large area %0.2f; volume %0.2f' % (Area[ndx], Vol[ndx]))
    area, vol, base = cylinder(h, r) # dimensions of the hole
    for ndx in np.arange(0, len(h)):
        print('small area %0.2f; volume %0.2f; base %0.2f' % (area[ndx], vol[ndx], base))
    # compute remaining volume
    Vol = Vol - 8*vol
    # the wetted area is a little messier. If we total the
    # large disk area and the areas of the holes, we get the
    # wetted area of the curved edges inside and out.
    # However, for each hole, the top and bottom areas have
    # been included not only in the top and bottom of the big
    # disk, but also as the contributions of each hole.
    # From the sum of the top areas, we therefore have to
    # remove 32 times the hole top area
    Area = Area + 8*(area - 2*base)
    for ndx in np.arange(0, len(h)):
        print('overall area %0.2f; volume %0.2f' % (Area[ndx], Vol[ndx]))
    
    
print("\nListing_03\n")
A = Listing_03();
