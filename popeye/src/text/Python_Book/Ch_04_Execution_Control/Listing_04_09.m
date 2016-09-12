% Listing 04.09 Script to compute liquid levels
another_tank = true;
while another_tank
    H = input('Overall tank height: ');
    r = input('tank radius: ');
    more_heights = true;
    while more_heights
        h = input('liquid height: ');
        if h < r
            v = (1/3)*pi*h.^2.*(3*r-h);
        elseif h < H-r
            v = (2/3)*pi*r^3 + pi*r^2*(h-r);
        elseif h <= H
            v = (4/3)*pi*r^3 + pi*r^2*(H-2*r) ...
                - (1/3)*pi*(H-h)^2*(3*r-H+h);
        else
            disp('liquid level too high')
            continue
        end
        fprintf( ...
            'rad %0.2f ht %0.2f level %0.2f vol %0.2f\n', ...
            r, H, h, v);
        more_heights = input('more levels? (y/n)','s')=='y';
    end
    another_tank = input('another tank? (y/n)','s')=='y';
end
