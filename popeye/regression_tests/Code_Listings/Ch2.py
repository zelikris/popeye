#% Listing 02.01 Script to solve for the hypotenuse
#clear
#clc
#A = 3; % the first side of a triangle
#B = 4; % the second side of a triangle
#hypSq = A^2 + B^2; % the square of the
#% hypotenuse
#H = sqrt(hypSq) % the answer
import math

def listing_01():
    A = 3 # the first side of a triangle
    B = 4 # the second side of a triangle
    hypSq = A**2 + B**2 #  the square of the hypotenuse
    H = math.sqrt(hypSq)
    return H

def listing_02_03():
    #% Listing 02.02 Script to compute the spacecraft's velocity (Part 1)
    #cmPerInch = 2.54; % general knowledge
    #inchesPerFt = 12; % general knowledge
    #metersPerCm = 1/100; % general knowledge
    #MetersPerFt = metersPerCm * cmPerInch * inchesPerFt;
    #startFt = 25000; % ft - given
    #startM = startFt * MetersPerFt
    cmPerInch = 2.54 # general knowledge
    inchesPerFt = 12 #  general knowledge
    metersPerCm = 1/100 #  general knowledge
    MetersPerFt = metersPerCm * cmPerInch * inchesPerFt
    startFt = 25000 #  ft - given
    startM = startFt * MetersPerFt
    #% Listing 02.03 Script to complete the computation of the spacecraft's velocity
    #g = 9.81 % m/sec^2
    #top = 100 % km - given
    #s = (top*1000) - startM % m
    #initialV = (2*g*s)^0.5 % the final answer
    g = 9.81 # m/sec^2
    top = 100 # m - given
    s = (top*1000) - startM # m
    initialV = (2*g*s)**0.5 # the final answer
    return initialV

