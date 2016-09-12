% Listing 13.04 Mirroring on a diagonal
function sq = diagMirror(A, code)
% mirror this square image diagonally
% the parameter code represents the number of
% 90 deg left rotations
for c = 1:3 % tacky to do a layer at a time, but
% tril must see a 2-D array
layer = A(:,:,c);
trin = tril(rot90(layer, code));
% rotate the image back after mirroring
sq(:,:,c) = rot90(trin + trin', 4 - code);
end
