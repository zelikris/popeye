% Listing 13.01 Exploring the sky situation
v = imread('Vienna.jpg');
image(v)
figure
row = 400;
red = v(row, :, 1);
gr = v(row, :, 2);
bl = v(row, :, 3);
plot(red, 'r');
hold on
plot(gr, 'g');
plot(bl, 'b');

fileXX8 = fopen( 'plotBLACK1m.txt', 'w');
for i = 1:size(bl,1)
    for j = 1:size(bl,2)
        fprintf( fileXX8, '%12.8f\n', bl(i, j));
    end
end
fclose(fileXX8);

fileYY8 = fopen( 'plotGREEN1m.txt', 'w');
for i = 1:size(gr,1)
    for j = 1:size(gr,2)
        fprintf( fileYY8, '%12.8f\n', gr(i, j));
    end
end
fclose(fileYY8);

fileZZ8 = fopen( 'plotRED1m.txt', 'w');
for i = 1:size(red,1)
    for j = 1:size(red,2)
        fprintf( fileZZ8, '%0.8f\n', red(i, j));
    end
end
fclose(fileZZ8);