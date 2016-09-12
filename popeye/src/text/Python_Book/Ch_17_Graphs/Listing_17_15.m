%   Listing 17.15 Testing graph search algorithms
makeGraph;   % call script to make the graph:
start = 1;
while start > 0
    gplot(A, coord, 'ro-')
    hold on
    for index = 1:length(coord)
        str = char('A' + index - 1);
        text(coord(index,1) + 0.2, ...
            coord(index,2) + 0.3, str);
    end
    axis([0 11 0 10]); axis off; hold on
    ch = input('Starting node: ','s');
    start = ch - 'A' + 1;
    if start > 0
        ch = input('Target node: ','s');
        target = ch - 'A' + 1;
        disp('original graph'); pause
        D = grBFS( A, start, target);
        gplot(D, coord, 'go-')
        disp('BFS result'); pause
        D = grDijkstra( A, start, target);
        gplot(D, coord, 'bo-')
        disp('Optimal result'); pause
        D = A_Star( A, start, target, coord);
        gplot(D, coord, 'm^-')
        disp('A* result'); pause
        hold off
    end
end
