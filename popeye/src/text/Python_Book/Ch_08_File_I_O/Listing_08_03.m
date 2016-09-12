% Listing 08.03 Script to copy a text file
ifn = input( 'input file name: ', 's' );
ofn = input('output file name: ', 's' );
ih = fopen( ifn, 'r' );
oh = fopen( ofn, 'w' );
ln = '';
while ischar( ln )
    ln = fgets( ih );
    if ischar( ln )
        fprintf( oh, ln );
    end
end
fclose( ih );
fclose( oh );
