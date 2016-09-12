% Listing 14.04 Plotting the spectrum of one instrument
function inst(name, ttl)
% plot the spectrum of the instrument with
% the given name, with the given plot title
[x, Fs] = wavread(['instr_' name '.wav']);
N = length(x);
dt = 1/Fs; % sampling period (sec)
t = (1:N) * dt; % time array for plotting
Y = abs(fft(x)); % perform the transform
mx = max(Y);
Y = Y * 100 / mx;
df = 1 / t(end) ; % the frequency interval
fmax = df * N / 2 ;
f = (1:N) * 2 * fmax / N;
up = floor(N/10);
plot(f(1:up), Y(1:up) );
title(ttl)
xlabel('Frequency (Hz)')
ylabel('Energy')
