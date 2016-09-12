clear
clc
close all
% Listing 04.08 Loop-and-a-half example
R = 1;
while R > 0
    R = input('Enter a radius: ');
    if R > 0
        area = pi * R^2;
        circum = 2 * pi * R;
        fprintf('area = %f; circum = %f\n', ...
            area, circum);
    end
end
