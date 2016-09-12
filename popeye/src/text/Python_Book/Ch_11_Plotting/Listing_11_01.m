% Listing 11.01 Creating a subplot
close all
x = -2*pi:.05:2*pi;
subplot(3,2,1)
plot(x, sin(x))
title('1 - sin(x)');
subplot(3,2,2)
plot(x, cos(x))
title('2 - cos(x)');
subplot(3,2,3)
plot(x, tan(x))
title('3 - tan(x)');
subplot(3,2,4)
plot(x, x.^2)
title('4 - x^2');
subplot(3,2,5)
plot(x, sqrt(x))
title('5 - sqrt(x)');
subplot(3,2,6)
plot(x, exp(x))
title('4 - e^x');

