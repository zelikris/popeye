% Listing 11.07 Simple surface plot
x=-3:3; y = x ;
[xx,yy]=meshgrid(x,y);
zz=xx.^2 + yy.^2;
mesh(xx,yy,zz)
axis tight
title('z = x^2 + y^2')
xlabel('x'),ylabel('y'),zlabel('z')

