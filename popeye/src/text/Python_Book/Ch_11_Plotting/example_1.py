from pylab import *

x = linspace(0, 5, 10)
y = x ** 2
figure()
subplot(1,2,1)
plot(x, y, 'r--')
subplot(1,2,2)
plot(y, x, 'g*-');
xlabel('x')
ylabel('y')
title('title')
