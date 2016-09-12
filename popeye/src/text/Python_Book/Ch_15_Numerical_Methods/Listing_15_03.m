% Listing 15.03 Eyeball linear estimation
x = 0:5;
y = [0 20 60 68 77 110];
y2 = 20 * x;
plot(x, y, 'o', x, y2);
axis([-1 7 -20 120])
title('Linear Estimate')
xlabel('Time (sec)')
ylabel('Temperature (degrees F)')
grid on
