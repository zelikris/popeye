% Listing 10.01 Country analysis
% build the country array
worldData = buildData('World_data.xls');
best = findBest(worldData);
fprintf('best country is %s\n', ...
    worldData(best).name)
