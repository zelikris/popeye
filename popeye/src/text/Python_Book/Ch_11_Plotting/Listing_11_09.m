% Listing 11.09 Constructing a sphere
facets = 120; radius = 1;
thr = linspace(0, 2*pi, facets); % range of theta
phir = linspace(0, pi, facets); % range of phi
[th, phi] = meshgrid( thr, phir );
x = radius * cos(phi);
y = radius * sin(phi) .* cos(th);
z = radius * sin(phi) .* sin(th);
surf(x, y, z);
shading interp
colormap copper
axis equal, axis tight, axis off
lightangle(60, 45)
