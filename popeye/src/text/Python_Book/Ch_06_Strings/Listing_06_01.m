% Listing 06.01 Encryption exercise
disp('original text')
txt = ['For example, consider the following:' 13 ...
'A = [4.7 1321454.47 4.8];' 13 ...
'index = 1;' 13 ...
'v = ''values'';' 13 ...
'str = sprintf(''%8s of A(%d) are \t%8.3f ' 13 ...
' v, index, A(index,1) ' 13 ...
'str = ' 13 ...
' values of A(1) are 4.700' 13 ...
'The first conversion, ''%8s'', took the value' ...
' of the first ' ...
'parameter, v, allowed 8 spaces. ' 13 ]
% % encryption section
rand('state', 123456)
loch = 33;
hich = 126;
range = hich+1-loch;
rn = floor( range * rand(1, length(txt) ) );
change = (txt>=loch) & (txt<=hich);
enc = txt;
enc(change) = enc(change) + rn(change);
enc(enc > hich) = enc(enc > hich) - range;
disp('encrypted text')
encrypt = char(enc)
% % good decryption
rand('state', 123456);
rn = floor( range * rand(1, length(txt) ) );
change = (encrypt>=loch) & (encrypt<=hich);
dec = encrypt;
dec(change) = dec(change) - rn(change) + range;
dec(dec > hich) = dec(dec > hich) - range;
disp('good decrypt');
decrypt = char(dec)
% % bad seed
rand('seed', 123457);
rn = floor( range * rand(1, length(txt) ) );
change = (encrypt>=loch) & (encrypt<=hich);
dec = encrypt;
dec(change) = dec(change) - rn(change) + range;
dec(dec > hich) = dec(dec > hich) - range;
disp('decrypt with bad seed')
decrypt = char(dec)
% % different generator
rand('seed', 123456)
rn = mod(floor( range * abs(randn(1, length(txt) ))/10 ),  ...
      range);
change = (encrypt>=loch) & (encrypt<=hich);
dec = encrypt;
dec(change) = dec(change) - rn(change) + range;
dec(dec > hich) = dec(dec > hich) - range;
disp('decrypt with wrong generator')
decrypt = char(dec)
