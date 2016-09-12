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
