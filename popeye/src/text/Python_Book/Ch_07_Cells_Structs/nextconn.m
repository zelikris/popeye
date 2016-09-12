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
