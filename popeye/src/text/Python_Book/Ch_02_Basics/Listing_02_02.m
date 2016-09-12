% Listing 02.02 Script to compute the spacecraft's velocity (Part 1)
cmPerInch = 2.54; % general knowledge
inchesPerFt = 12; % general knowledge
metersPerCm = 1/100; % general knowledge
MetersPerFt = metersPerCm * cmPerInch * inchesPerFt;
startFt = 25000; % ft - given
startM = startFt * MetersPerFt
