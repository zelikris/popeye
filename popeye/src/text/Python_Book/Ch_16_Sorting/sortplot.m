clear
clc
clf
load sortdata;
lowerLim = 1.e-4;
sl(sl < lowerLim) = lowerLim;
loglog(sz, sl*100);
hold on;
title('Comparison of Sort Algorithms');
xlabel('Number of Items Sorted (log scale)');
ylabel('Relative Sort Time (log scale)');
in(in < lowerLim) = lowerLim;
loglog(sz, in*1000, 'g.');
bub(bub < lowerLim) = lowerLim;
loglog(sz, bub*1000, '--c');
mg(mg < lowerLim) = lowerLim;
loglog(sz,mg,'.');
qk(qk < lowerLim) = lowerLim;
loglog(sz,qk,'--');
ml(ml < lowerLim) = lowerLim;
loglog(sz,ml,'.-');
n = [20 maxSize];
nsq = n .* n / 15000;
nlogn = n .* log(n) / 300000;
loglog(n, nsq, 'r');
loglog(n, nlogn, 'r--'); 
legend('Selection','Insertion','Bubble', 'Merge','Quick', ...
    'Matlab', 'N squared', 'N log N', 2);
