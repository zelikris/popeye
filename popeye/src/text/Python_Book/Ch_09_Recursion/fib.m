% Listing 09.05 The Fibonacci function
function result = fib(N)
% recursive computation the Nth Fibonacci number
    if N == 1 || N == 2
        result = 1;
    else
        result = fib(N-1) + fib(N-2);
    end
end
