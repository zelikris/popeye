% Listing 09.07 Recursive root finding
function pt = findZero(x)
% x is a lower-upper pair guaranteed to have
% y values of opposite sign
% return the x coordinate of the root
    if abs(x(1)-x(2)) < .001
        pt = x(1);
    else
        mx = sum(x)/2;
        my = f(mx);
        if my*f(x(1)) <= 0
            pt = findZero([x(1) mx]);
        else
            pt = findZero([mx x(2)]);
        end
    end
end
