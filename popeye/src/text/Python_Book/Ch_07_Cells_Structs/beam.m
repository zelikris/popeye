function ans = beam( nm, xp, yp, conn )
% construct a beam structure with fields:
% name - beam name
% xp, yp - coordinates of its centroid
% conn - cell array - names of adjacent beams
% useage: ans = beam( nm, xp, yp, conn )
    ans.name = nm;
    ans.pos = [xp, yp];
    ans.connect = conn;
end
