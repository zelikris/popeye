% Listing 05.03 Volume and area of a disk
h = 1:5; % set a range of disk thicknesses
R = 25;
r = 3;
[Area Vol] = cylinder(h, R) % dimensions of large disk
[area vol] = cylinder(h, r) % dimensions of the hole
% compute remaining volume
Vol = Vol - 8*vol
% the wetted area is a little messier. If we total the
% large disk area and the areas of the holes, we get the
% wetted area of the curved edges inside and out.
% However, for each hole, the top and bottom areas have
% been included not only in the top and bottom of the big
% disk, but also as the contributions of each hole.
% From the sum of the top areas, we therefore have to
% remove 32 times the hole top area
Area = Area + 8*(area - 2*2*pi*r.^2)
