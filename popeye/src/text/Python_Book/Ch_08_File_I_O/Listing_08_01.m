% Listing 08.01 Script to list a text file
fn = input( 'file name: ', 's' );
fh = fopen( fn, 'r' );
ln = '';
while ischar( ln )
    ln = fgets( fh );
    if ischar( ln )
        fprintf( ln );
    end
end
fclose( fh );
