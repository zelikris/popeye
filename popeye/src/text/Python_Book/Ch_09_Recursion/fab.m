% Listing 09.09 Function for zeros
function res = fab(beta)
% f(beta) = r1 (cos(alpha) + sin(alpha) - 1)
% + r2 (cos(beta) + sin(beta) - 1)
global r1
global r2
global alpha
res = r1 * (cos(alpha) + sin(alpha) - 1) ...
       + r2 * (cos(beta) + sin(beta) - 1);
