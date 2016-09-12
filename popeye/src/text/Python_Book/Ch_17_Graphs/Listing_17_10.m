% Listing 17.10 Prim's Algorithm to compute a MST
makeGraph
A = grAdjacency( node, cost, dir )
start = 1;
gplot(A, coord, 'ro-')
hold on
for index = 1:length(coord)
     str = char('A' + index - 1);
     text(coord(index,1) + 0.2, ...
          coord(index,2) + 0.3, str);
end
axis([0 11 0 10]); axis off; hold on
N = start;
running = true;
result = sparse([0]);
while running
   % find the smallest edge 
   best = 10000;
   running = false;
   for ndx = 1:length(N)
        node = N(ndx);
        next = find(A(node,:) > 0);
        for nxt = 1:length(next)
            nxtn = next(nxt);
            if ~any(N == nxtn)
                running = true;
                if A(node, nxtn) < best
                    best = A(node, nxtn);
                    from = node;
                    to = nxtn;
                end
            end
        end
   end
   if running
       N = [N to];
       result(from, to) = 1;
   end
end
gplot(result, coord, 'gx--')
