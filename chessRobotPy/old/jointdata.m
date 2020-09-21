function [j1, j2, j36] = jointdata(posX, posY)
L = size(posX);
for i = 1:L
    x = posX(i); y = posY(i); srctheta2 = 43; srctheta3 = -85;
    robotX = 501; robotY = -213;
    pxldis = 0.0312;
    d = pxldis * sqrt((x-robotX)^2 + (y-robotY)^2);
    
    degree = atand((y-robotY) / (robotX-x));
    if degree < 0
        degree = 180 + degree;
    end
    j1(:,i) = fix(degree * 19.64);
    
    p = sqrt(8.55^2 +d^2);
    theta_a = atand(8.55 / d);
    theta_b = acosd((17.78^2 + 17.78^2 - p^2) / (2*17.78*17.78));
    theta_c = (180 - theta_b) / 2;
    theta_3 = -(theta_a + theta_c);
    theta_2 = 180 - theta_a - theta_b - theta_c;
    
    j36(:,i) = fix(-(theta_3 - srctheta3)* 11.765);
    j2(:,i) = fix(-(theta_2 - srctheta2) * 19.5);
end
end
