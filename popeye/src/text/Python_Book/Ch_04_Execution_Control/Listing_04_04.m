% Listing 04.04 Example of a switch statement
switch month
   case {9, 4, 6, 11}
   % Sept, Apr, June, Nov
       days = 30;
    case 2 % Feb
       if leapYear
           days = 29;
       else
           days = 28;
       end
    case {1, 3, 5, 7, 8, 10, 12}
        % other months
        days = 31;
    otherwise
        error('bad month index')
end
