% Listing 14.06 Synthesizing a piano
 [snd Fs] = wavread('instr_piano.wav');
 N = length(snd);
 sound(snd, Fs)
 tMax = N / Fs;
 dt = 1 / Fs;
 Y = fft(snd);
 Ns = N/4;
 fMax = Fs/4;
 df = fMax / Ns;
f = ((1:Ns) - 1) * df;
rl = real(Y(1:Ns));
im = imag(Y(1:Ns));
plot(f, abs(Y(1:Ns)))
xlabel('frequency (Hz)')
ylabel('real amplitude')
zlabel('imag amplitude')
amps = abs(Y(1:end/2));
Nc = 25;
for ndx = 1:Nc
    [junk where] = max(amps);
    C(ndx).freq = where;
    C(ndx).coeff = Y(where);
   amps(where-25:where+25) = 0;
end
frq = [C.freq];
[frq order] = sort(frq);
sortedStr = C(order);
Nt = 25;
t = (1:2*Fs) * dt;
f = zeros(1, length(t));
for ndx = 1:Nt
 w = frq(ndx) * df * 2 * pi;
    ct = cos(w*t);
    st = sin(w*t);
    Cf = sortedStr(ndx).coeff;
    f = f + real(Cf) * ct + imag(Cf) * st;
end
% amplitude shaping goes here
sf = f ./ max(f);
sound(sf, Fs)
