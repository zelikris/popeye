% Listing 5.1 - cylinder function
function volume = cylinder(height, radius)
% function to compute the volume of a cylinder
% volume = cylinder(height, radius)
    base = pi * radius^2
    volume = base * height
end
