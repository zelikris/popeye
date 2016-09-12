from math import pi

def Listing_01(height, radius):
    """
        This function computes the volume of a cylinder
        based on the given height and radius
        @param height float The height of the cylinder
        @param radius float The radius of the cylinder
        @return float The volume of the cylinder
    """
    # the base of a cylinder is the product of pi and the
    # radius raised to the second power
    base = pi * (radius ** 2)
    # the volume of a cylinder is the product of base and
    # the height
    #
    # return this value as the volume
    return (base * height)

def Listing_02(height, radius):
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
