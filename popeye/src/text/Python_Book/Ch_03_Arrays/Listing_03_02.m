% Listing 03.02 Script to solve vector problems
PA = [0 1 1]
PB = [1 1 0]
P = [2 1 1]
M = [4 0 1]
% find the resultant of PA and PB
PC = PA + PB
% find the unit vector in the direction of PC
mag = sqrt(sum(PC.^2))
unit_vector = PC/mag
% find the moment of the force PC about M
% this is the cross product of MP and PC
MP = P - M
moment = cross( MP, PC )
