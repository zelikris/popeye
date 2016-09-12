% Listing 17.11 Breadth-first graph search
function D = grBFS(A, home, target)
q = qEnq([], home);
while ~isempty(q)
    [q current] = qDeq(q);
    if current(end) == target % success exit
        D = sparse([0]);
        for it = 1:length(current)-1
            D(current(it), current(it+1)) = 1;
        end
        return; % exit the function
    end % if current == target
    thisNode = current(end);
    children = find(A(thisNode,:) ~= 0);
    for thisChild = children
        if ~any(thisChild == current)
            q = qEnq(q, [current thisChild]);
        end % if ~any(thisChild == current)
    end % for thisChild = children
end % while q not empty
% if we reach here we never found a path
D = [];
end
