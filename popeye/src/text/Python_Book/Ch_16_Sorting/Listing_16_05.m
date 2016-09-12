% Listing 16.05 Updated world data analysis
function doit
    worldData = buildData('World_data.xls');
    n = 20;
    bestn = findBestn(worldData, n);
    fprintf('best %d countries are:\n', n)
    for best = bestn(end:-1:1)
        fprintf('%s\n', worldData(best).name)
    end
end
function bestn = findBestn(worldData, n)
% find the indices of the n best countries
% according to the criterion in the function fold
% we first map world data to add the field growth
    for ndx = 1:length(worldData)
        cntry = worldData(ndx);
        worldData(ndx).growth = fold(cntry);
    end
    % now, sort on this criterion
    values = [worldData.growth];
    [junk order] = sort(values);
    % filter these to keep the best 10
    bestn = order(end-n+1:end);
end
function ans = fold(st)
% s1 is the rate of growth of population
    pop = st.pop(~isnan(st.pop));
    yr = st.year(~isnan(st.pop));
    s1 = slope(yr, pop)/mean(pop);
    % s2 is the rate of growth of the GDP
    gdp = st.gdp(~isnan(st.gdp));
    yr = st.year(~isnan(st.gdp));
    s2 = slope(yr, gdp)/mean(gdp);
    % Measure of merit is how much faster
    % the gdp grows than the population
    ans = s2 - s1;
end
function sl = slope(x, y)
% Estimate the slope of a curve
    if length(x) == 0 || x(end) == x(1)
        error('bad data')
    else
        coef = polyfit(x, y, 1);
        sl = coef(1);
    end
end
