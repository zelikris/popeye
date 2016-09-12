#!/usr/bin/env python

# pi constant from math library
from math import pi

# Cylinder function from Listing_05_02.py
def cylinder(height, radius):
    base = pi * (radius ** 2)
    volume = base * height
    area = (2 * base) + (height * 2 * base)
    return {"area" : area, "volume" : volume}

# ------------------------------ 
#   ORIGINAL CODE
# ------------------------------ 
# % Listing 05.03 Volume and area of a disk
# h = 1:5; % set a range of disk thicknesses
# R = 25;
# r = 3;
# [Area Vol] = cylinder(h, R) % dimensions of large disk
# [area vol] = cylinder(h, r) % dimensions of the hole
# % compute remaining volume
# Vol = Vol - 8*vol
# % the wetted area is a little messier. If we total the
# % large disk area and the areas of the holes, we get the
# % wetted area of the curved edges inside and out.
# % However, for each hole, the top and bottom areas have
# % been included not only in the top and bottom of the big
# % disk, but also as the contributions of each hole.
# % From the sum of the top areas, we therefore have to
# % remove 32 times the hole top area
# Area = Area + 8*(area - 2*2*pi*r.^2)

# starting and ending integer values for the heights
height_start = 1
height_end_exclusive = 6

# set a range of disk thicknesses: [1, 2, 3, 4, 5]
# the range() function is exclusive on the end bound
# so we use 6 to generate [1, 2, 3, 4, 5]
h = range(height_start, height_end_exclusive)
R = 25
r = 3

# area/volume of the large disk
# each index contains a dictionary with the volume/area for each
# incrementing value of h
large_disk = []
for height in h:
    large_disk.append(cylinder(height, R))

# area/volume of the hole
hole = []
for height in h:
    hole.append(cylinder(height, r))

# remaining volume after removing hole's volume
remaining_volume = []
for index in range(len(large_disk)):
    volume = large_disk[index]['volume'] - (8 * hole[index]['volume'])
    remaining_volume.append(volume)

# wetted area's volume
wetted_area = []
for index in range(len(large_disk)):
    area = large_disk[index]['area'] + (8 * (hole[index]['area'] - 2 * 2 * pi * r ** 2))
    wetted_area.append(area)
