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
