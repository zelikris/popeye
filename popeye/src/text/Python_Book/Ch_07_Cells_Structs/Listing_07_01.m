% Listing 07.01 Using cell arrays of parameters
A = 4;
B = 6;
C = 5;
N = largest(A, B, C)
params = { 4, 6, 5 };
N = largest(params{1:3})
