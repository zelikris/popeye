% Listing 13.03 Making a kaleidoscope
sb = imread('sqbutter.jpg');
subplot( 1, 2, 1);
image(sb);
cols = length(sb);
mid = cols/2
subplot( 1, 2, 2);
img = [diagMirror( sb(1:mid, 1:mid, :), 0 ) ...
diagMirror( sb(1:mid, mid+1:end, :), 3 );
diagMirror( sb(mid+1:end, 1:mid, :), 1 ) ...
diagMirror( sb(mid+1:end, mid+1:end, :), 2 )];
image(img);
