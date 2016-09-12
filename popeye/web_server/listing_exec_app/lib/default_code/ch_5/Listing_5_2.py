#!/usr/bin/env python

# ------------------------------ 
#   ORIGINAL CODE
# ------------------------------ 
# % Listing 05.02 cylinder function with multiple results
# function [area, volume] = cylinder(height, radius)
# % function to compute the area and volume of a cylinder
# % usage: [area, volume]=cylinder(height, radius)
#     base = pi * radius^2
#     volume = base * height
#     area = 2 * pi * radius .* height + 2 * base
# end


def cylinder(height, radius):
    """
        This function computes the volume of a cylinder
        based on the given height and radius

        @param height float The height of the cylinder
        @param radius float The radius of the cylinder

        @return dictionary An associative array with the key
                           'area' corresponding to the area
                           and 'volume' corresponding to the
                           volume of the cylinder
    """
    # for the use of pi
    from math import pi
    # calculate the base of the cylinder
    # pi times r squared
    base = pi * (radius ** 2)
    # calculate the volume of the cylinder
    # base times height
    volume = base * height
    # calculate the area of the cylinder
    # (2 * pi * r^2) + h(2 * pi * r^s)
    # 
    # NOTE: 2 * pi * r^2 = 2 * base
    area = (2 * base) + (height * (2 * base))
    return {"area" : area, "volume" : volume}
