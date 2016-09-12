% Listing 07.06 Connectivity of a structure
data(1) = beam('A-1', 0.866, 0.5, ...
           {'A','A-2','A-3','D-1'} );
data(2) = beam('A-2', 0, 1, ...
           {'A','A-3','B-1','B-2'} );
data(3) = beam('A-3', 0.866, 1.5, ...
           {'A-1','A-2','B-1','D-1'} );
data(4) = beam('B-1', 0.866, 2.5, ...
           {'A-2','A-3','B-2','B-3','D-1','D-2'} );
data(5) = beam('B-2', 0, 3, ...
           {'A-2','A-3','B-1','B-3','C-1','C-2'} );
data(6) = beam('B-3', 0.866, 3.5, ...
           {'B-1','B-2','C-1','C-2','D-1','D-2'} );
data(7) = beam('C-1', 0.866, 4.5, ...
           {'B-2','B-3','C-2','C-3','D-2'} );
data(8) = beam('C-2', 0, 5, ...
           {'B-2','B-3','C-1','C-3','C'} );
data(9) = beam('C-3', 0.866, 5.5, ...
           {'C-1','C-2','D-2','C'} );
data(10) = beam('D-1', 1.732, 2, ...
           {'A-1','A-3','B-1','B-3','D-2'} );
data(11) = beam('D-2', 1.732, 4, ...
           {'B-1','B-3','C-1','C-3','D-1'} )
conn = 'A';
clist = {conn};
while true
    index = 0;
    % find all the beams connected to conn
    for in = 1:length(data)
        str = data(in);
        if touches(str, conn)
            index = index + 1;
            found(index) = str;
        end
    end  
    % eliminate those already connected
    for jn = index:-1:1
        if ison(found(jn).name, clist)
            found(jn) = [];
        else
            clist = [clist {found(jn).name}]
        end
    end
    if length(found) > 0
        conn = nextconn( found, clist )
        clist = [clist conn];
    else
        break;
    end
end
disp('the order of assembly is:')
disp(clist)
