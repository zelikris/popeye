% Listing 12.02 Simulating stars
nst = 20; th = 0;
for ndx = 1:nst
    pos(ndx,:) = rand(1,2)*10;
    scale(ndx) = rand(1,1) * .9 + .1;
    rate(ndx) = rand(1,1) * 3 + 1;
end
while true
    for str = 1:nst
        star(pos(str,:), ... % location
            scale(str), ... % scale
            th, ... % basic angle
            rate(str)) % angle multiplier
    end
    colormap autumn
    axis equal; axis([-.5 10.5 -.5 10.5])
    axis off; hold off
    th = mod(th + .1, 20*pi);
    pause(0.1)
end
