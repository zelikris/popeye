% Listing 09.02 script using exception processing
OK = false;
while ~OK
    try
        side = input('enter a triangle: ');
        a = side(1); b = side(2); c = side(3);
        cosC = (c^2 - a^2 - b^2)/(2 * a * b);
        angle = acosd(cosC);
        if imag(angle) ~= 0
            error('bad triangle')
        end
    catch
        disp('bad triangle - try again')
    end
    OK = true;
end
fprintf('the angle is %f\n', angle)
