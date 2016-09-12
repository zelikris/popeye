% Listing 09.08 Finding arm position
global r1
r1 = 4
global r2
r2 = 3
global alpha
alpha = pi/6 % 30 deg
beta = linspace(-pi, pi, 19);
pf = fab(beta);
zeros = find(pf(1:end-1) .* pf(2:end) <= 0)
disp('zeros occur just after')
beta(zeros)
%
zero = findZeroAB([beta(zeros(1)) ...
        beta(zeros(1)+1)])
