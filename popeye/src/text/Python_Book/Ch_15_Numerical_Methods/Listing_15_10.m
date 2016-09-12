% Listing 15.10 modifying sound amplitude
figure
plot(snd)
hold on
incr = 1000;
at = 1;
samples = [];
tm = [];
while at < (N - incr)
   val = max(snd(at:at+incr-1));
   samples = [samples val];
   tm = [tm at+incr/2];
   at = at + incr;
end
plot(tm, samples,'r*')
coeff = polyfit(tm, samples, 8);
samp = polyval(coeff, tm);
plot(tm, samp, 'c')
amult = polyval(coeff, 1:length(f));
f = f .* amult;
sf = f ./ max(f);
sound(sf, Fs)
