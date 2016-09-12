% Listing 14.02 Building a tune file
[note, Fs] = wavread('instr_piano.wav');
half = 2^(1/12);
doremi = [1 3; 2 1; 3 3; 1 1; 3 2; 1 2; 3 4; 2 3;
    3 1; 4 1; 4 1; 3 1; 2 1; 4 8; 3 3; 4 1;
    5 3; 3 1; 5 2; 3 2; 5 4; 4 3; 5 1; 6 1;
    6 1; 5 1; 4 1; 6 4 ];
steps = [0 2 4 5 7 9 11 12];
dt = .2;
nCt = floor(dt*Fs);
storeAt = 1;
for index = 1:length(doremi)
    key = doremi(index,1);
    pow = steps(key);
    theNote = note(ceil(1:half^pow:end));
    noteLength = length(theNote);
    noteEnd = storeAt + noteLength - 1;
    tune(storeAt:noteEnd,1) = theNote;
    storeAt = storeAt + doremi(index,2) * nCt;
end
sound(tune, Fs)
wavwrite(tune, Fs, 'dohAdeer.wav')
