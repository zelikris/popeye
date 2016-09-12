% Listing 14.01 Play a scale by shrinking the note
[note, Fs] = wavread('instr_piano.wav');
half = 2^(1/12);
whole = half^2;
for index = 1:8
    sound(note, Fs);
    if (index == 3) || (index == 7)
        mult = half;
    else
        mult = whole;
    end
    note = note(ceil(1:mult:end));
end;
