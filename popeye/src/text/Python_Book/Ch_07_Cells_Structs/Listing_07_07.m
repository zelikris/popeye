% Listing 07.07 Support functions
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
function res = touches(beam, conn)
% does the beam touch this connecting point?
% usage: res = touches(beam, conn)
    res = false;
    for in = 1:length(beam.connect)
        item = beam.connect{in};
        if strcmp(item,conn)
            res = true; break;
        end
    end
end
function res = ison( nm, cl )
% is this beam on the connection list,
% a cell array of beam names
% usage: res = ison( beam, cl )
    res = false;
    for in = 1:length(cl)
        item = cl{in};
        if strcmp(item, nm)
            res = true; break;
        end
    end
end
function nm = nextconn( fnd, cl )
% find a connection name among
% those found not already connected
% usage: nm = nextconn( fnd, cl )
    for in = 1:length(fnd)
        item = fnd(in);
        cn = item.connect;
        for jn = 1:length(cn)
            nm = cn{jn};
            if ~ison(nm, cl)
                break;
            end
        end
    end
end
