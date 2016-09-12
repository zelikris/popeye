% Listing 17.01 Enqueue and dequeue functions
function q = qEnq(q, data)
% enqueue onto a queue
q = [q {data}];
