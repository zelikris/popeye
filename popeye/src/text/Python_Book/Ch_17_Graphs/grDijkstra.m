% Listing 17.13 Code for Dijkstra's algorithm
function D = grDijkstra(A, home, target)
    pq = pqEnq([], Path(home, 0));
    while ~isempty(pq)
        [pq current] = qDeq(pq);
        if pthGetLast(current) == target
            D = sparse(0);
            answer = current.nodes;
            for it = 1:length(answer)-1
                D(answer(it), answer(it+1)) = 1;
            end
            return;
        end % if last(current) == target
        endnode = pthGetLast(current);
        children = A(endnode,:);
        children = find(children ~= 0);
        for achild = children
            len = A(endnode, achild);
            if ~any(achild == current.nodes)
                gclone = Path( [current.nodes achild], ...
                    current.key + len);
                pq = pqEnq(pq, gclone);
            end % if ~any child == current.nodes
        end % for achild = children
    end % if pq not empty
    % If we reach here we never found a path
    D = [];
end
