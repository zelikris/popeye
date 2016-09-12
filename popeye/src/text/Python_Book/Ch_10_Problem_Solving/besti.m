% Listing 10.03 Folding the country data
function besti = findbest(worldData)
% find the index of the best country
% according to the criterion in the function
% fold
    best = fold(worldData(1));
    besti = 1;
    for ndx = 2:length(worldData)
        cntry = worldData(ndx);
        tryThis = fold(cntry);
        if tryThis > best
            best = tryThis;
            besti = ndx;
        end
    end
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
        sl = (y(end) - y(1))/(x(end) - x(1));
    end
end
