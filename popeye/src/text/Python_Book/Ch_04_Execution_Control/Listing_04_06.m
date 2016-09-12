% Listing 04.06 for statement using indexing
A = floor(rand(1,10)*100)
theMax = A(1);
theIndex = 1;
for index = 1:length(A)
    x = A(index);
    if x > theMax
        theMax = x;
        theIndex = index;
    end
end
fprintf('the max value in A is %d at %d\n', ...
    theMax, theIndex);
