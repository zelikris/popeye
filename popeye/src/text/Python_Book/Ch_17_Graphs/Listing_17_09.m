% Listing 17.09 Breadth-first graph traversal
makeGraph
% Constructs an adjacency matrix
start = 5;
% start is a node number (in this case, 'E')
% Create a queue and
% enqueue a path containing home
q = qEnq([], start);
% initialize the visited list
visited = start;
% initialize the result
fprintf('trace: ')
% While the queue is not empty
while ~isempty(q)
    % Dequeue a path
    [q thisNode] = qDeq(q);
    % Traverse the children of this node
    fprintf('%s - ', char('A'+thisNode-1) );
    children = find(A(thisNode,:) ~= 0);
    for aChild = children
        % If the child is not on the path
        if ~any(aChild == visited)
            % Enqueue the new path
            q = qEnq(q, aChild);
            % add to the visited list
            visited = [visited aChild];
        end % if ~any(eachchild == current)
    end % for eachchild = children
end % while q not empty
fprintf('\n');

