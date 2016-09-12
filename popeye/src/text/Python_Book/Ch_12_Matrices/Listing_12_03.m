% Listing 12.03 Drawing one star
function star(pt, sc, v, th)
% draw a star at pt(1), pt(2),
% scaled with sc, at angle v*th
    triangle(1, v*th, pt, sc) 
    hold on
    triangle(-1, v*th, pt, sc)
end
function triangle( up, th, pt, sc )
    pts = [-.5    .5    0   -.5; % x values
           -.289 -.289 .577 -.289]; % y values
    % rotation matrix
    A = sc * [cos(th), -sin(th); sin(th), cos(th)];
    thePts = A * pts;
    fill( thePts(1,:) + pt(1), ...
          up*thePts(2,:) + pt(2), 1);
end
