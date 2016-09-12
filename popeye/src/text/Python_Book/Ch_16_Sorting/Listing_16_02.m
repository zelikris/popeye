% Listing 16.02 Bubble sort
function bubblesort()
% This function sorts the column array b in place,
% using the bubble sort algorithm
    global b
    N = length(b);
    right = N-1;
    for in = 1:(N-1)
        for jn = 1:right
            if gt(b(jn), b(jn+1))
                tmp = b(jn); % swap b(jn) with b(jn+1)
                b(jn) = b(jn+1);
                b(jn+1) = tmp;
            end
        end
        right = right - 1;
    end
end
