% Listing 04.05 Example of a for statement
A = [6 12 6 91 13 6] % initial vector
theMax = A(1); % set initial max value
for x = A % iterate through A
    if x > theMax % test each element
        theMax = x;
    end
end
fprintf('max(A) is %d\n', theMax);
