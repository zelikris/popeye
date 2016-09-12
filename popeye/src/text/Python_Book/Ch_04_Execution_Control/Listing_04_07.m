% Listing 04.07 while statement example
A = floor(rand(1,10)*100)
theMax = A(1);
theIndex = 1;
index = 1;
while index <= length(A)
    x = A(index);
    if x > theMax
       theMax = x;
       theIndex = index;
    end
    index = index + 1;
end
fprintf('the max value in A is %d at %d\n', ...
                                        theMax, theIndex);
