% Listing 16.03 Quick sort
function a = quicksort(a, from, to)
% This function sorts a column array,
% using the quick sort algorithm
    if from < to
        [a p] = partition(a, from, to);
        a = quicksort(a, from, p);
        a = quicksort(a, p + 1, to);
    end
end
function [a lower] = partition(a, from, to)
% This function partitions a column array
    pivot = a(from); i = from - 1; j = to + 1;
    while i < j
        i = i + 1;
        while lt(a(i), pivot)
            i = i + 1;
        end
        j = j - 1;
        while gt(a(j), pivot)
            j = j - 1;
        end
        if i < j
            temp = a(i); % this section swaps
            a(i) = a(j); % a(i) with a(j)
            a(j) = temp;
        end
    end
    lower = j;
end

