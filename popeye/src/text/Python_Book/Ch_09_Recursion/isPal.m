% Listing 09.04 Recursive palindrome detector
function ans = isPal(str)
    % recursive palindrome detector
    if length(str) < 2
        ans = true;
    elseif str(1) ~= str(end)
        ans = false;
    else
        ans = isPal(str(2:end-1));
    end
end
