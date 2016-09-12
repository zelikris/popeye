% Listing 16.01 The insertion sort function
function b = insertionsort(a)
% This function sorts a column vector,
% using the insertion sort algorithm
    b = []; i = 1; sz = length(a);
    while i <= sz
        b = insert(b, a(i,1) );
        i = i + 1;
    end
end
function a = insert(a, v)
% insert the value v into column vector a
    i = 1; sz = length(a); done = false;
    while i <= sz
        if lt(v, a(i,1))
            done = true;
            a = [a(1:i-1); v; a(i:end)];
            break;
        end
        i = i + 1;
    end
    if ~done
        a(sz+1, 1) = v;
    end
end
