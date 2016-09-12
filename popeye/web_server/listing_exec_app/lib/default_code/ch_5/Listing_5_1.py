#!/usr/bin/env python

# ------------------------------ 
#   ORIGINAL CODE
# ------------------------------ 
# Listing 5.1 - cylinder function
# function volume = cylinder(height, radius)
# % function to compute the volume of a cylinder
# % volume = cylinder(height, radius)
#     base = pi * radius^2
#     volume = base * height
# end

def cylinder(height, radius):
    """
        This function computes the volume of a cylinder
        based on the given height and radius

        @param height float The height of the cylinder
        @param radius float The radius of the cylinder

        @return float The volume of the cylinder
    """
    # need math to use pi constant
    from math import pi
    # the base of a cylinder is the product of pi and the
    # radius raised to the second power
    base = pi * (radius ** 2)
    # the volume of a cylinder is the product of base and
    # the height
    #
    # return this value as the volume
    return (base * height)
