% Listing 11.08 Constructing a cylinder
facets = 120; len = 2; radius = 1;
thr = linspace(0, 2*pi, facets);
xr = [0 len];
[xx, tth] = meshgrid( xr, thr );
yy = radius * cos(tth);
zz = radius * sin(tth);
surf(xx, yy, zz);
shading interp
colormap bone
axis equal,axis tight,axis off
lightangle(60, 45)
alpha(0.8)
view(-20, 35)
