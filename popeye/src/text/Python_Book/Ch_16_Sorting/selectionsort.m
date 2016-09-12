function b = selectionsort(a)
%
%   This program sorts an array, using the selection sort 
%   algorithm
%
    b = a;
    for i = 1 : size(b)
        j = minimumPosition(b, i);
%        swap(a, i, j);
          temp = b(i);
          b(i) = b(j);
          b(j) = temp;
    end
     
function ans = minimumPosition(a, from)
%
%      Finds the smallest element in a tail range of the array
%      from is the first position in a to compare
%      return the position of the smallest element in the
%      range a[from]...a[a.length]
%
     ans = from;
     for i = from : length(a)
         if a(i) < a(ans) 
%             disp(sprintf('smallest at: %d', i));
             ans = i;
         end
     end
