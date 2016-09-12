% Listing 09.10 Recursive zero finder
function pt = findZeroAB(x)
% x is a lower-upper pair guaranteed to have
% y values of opposite sign
    y = fab(x);
    if abs(x(1)-x(2)) < .001
        pt = [x(1) y(1)];
    else
        mx = sum(x)/2;
        my = fab(mx);
        if my*y(1) < 0
            pt = findZeroAB([x(1) mx]);
        else
            pt = findZeroAB([mx x(2)]);
        end
    end
end
