function [chess,order,index,prior] = calcu_position(predicted,posX,posY)
load chesslocation.mat
L = size(posX,1);
%x = posX; y = posY;
for i = 1:L
    x = posX(i); y = posY(i);
    %camposi_x = 700; camposi_y = 440; camposi_xh = 1500; camposi_yh = 1500;
    camposi_x = 682.3; camposi_y = 494.7; camposi_xh = 1508; camposi_yh = 1509;
    %-------------------------
    chess_h = 32.05;
    x = round(x +((chess_h * (camposi_x - x)) / camposi_xh),1);
    y = round(y +((chess_h * (camposi_y - y)) / camposi_yh),1);
    src = [x,y,1]';
    thx = 180;
    rotx = [1 0 0;0 cosd(thx) -sind(thx);0 sind(thx) cosd(thx)];
    thz = 180.3;%181
    rotz = [cosd(thz) -sind(thz) 0;sind(thz) cosd(thz) 0;0 0 1];
    scale = [1 0 0;0 1 0;0 0 1];
    %tran = [1 0 -475;0 1 187;0 0 1];
    tran = [1 0 -475;0 1 187;0 0 1];
    %---------------------------------------------
    new(i,:) = (round((rotx * rotz * scale * tran * src),2))';
    nxy(i,:) = new(i,1:2);
    rx = nxy(i,1); ry = nxy(i,2);
    degree = atan2d(ry,rx);
    j1(i) = round(degree * 19.64);
    %--------------------------------------------
    %{
    if x <= 491
        thz1 = 180.208; %181.1
        rotz = [cosd(thz1) -sind(thz1) 0;sind(thz1) cosd(thz1) 0;0 0 1];
        scale = [1.04 0 0;0 1.011 0;0 0 1];%1.04 1.011
        tran = [1 0 -483.6;0 1 209.6;0 0 1];%-483.6 209.6
    else
        thz1 = 180.208; %180.3
        rotz = [cosd(thz1) -sind(thz1) 0;sind(thz1) cosd(thz1) 0;0 0 1];
        scale = [1.0027 0 0;0 1.0114 0;0 0 1];%1.0027 1.0114
        tran = [1 0 -482.3;0 1 187.3;0 0 1];%-482.3 187.3
    end
    new1 = (round((rotx * rotz * tran * scale * src),2))';
    nxy1 = new1(1,1:2);
    %}
    new1 = new;
    nxy1 = nxy;
    rx1 = nxy1(1,1); ry1 = nxy1(1,2);
    
    %srctheta2 = 42.7; 
    srctheta2 = 41.3;
    %-------------
    srctheta3 = -89;
    %--------------
    pxldis = 0.0312;
    d = round(pxldis * sqrt(rx1^2 + ry1^2),2);
    d_src = d;
    
        
    if d > 34.5
        d = 34.5;
        d_dif = d_src(i) - d;
        j45_theta = asind(d_dif/9.2);
        j45(i) = round(-j45_theta * 4.27);
        j45_rotate(i) = 0;
    else
        j45(i) = 0;
        j45_rotate(i) = round((degree-90) * 4.27);
        if abs(j45_rotate(i)) < 15
            j45_rotate(i) = 0;
        end
    end
    
    p = sqrt(8.54^2 +d^2);
    theta_a = atand(8.55 / d);
    theta_b = acosd((17.78^2 + 17.78^2 - p^2) / (2*17.78*17.78));
    theta_c = (180 - theta_b) / 2;
    theta_3 = -(theta_a + theta_c);
    theta_2 = 180 - theta_a - theta_b - theta_c;
    
    j36(i) = round(-(theta_3 - srctheta3)* 11.55);
    j2(i) = round(-(theta_2 - srctheta2) * 19.64);
end

currentj1 = 0;
currentj36 = 0;
chess = [j1' j2' j36' j45' j45_rotate'];
b = [7 9 5 3 1 2 4 8 6 23 25 21 19 17 18 20 24 22 11 10 27 26 33 16 12 15 13 14 32 28 31 29 30];
for p = 1:33
    prior(p,:) = chesslocation(b(p),:);
end
order = zeros(L(1),5);
for a = 1:L
    k = size(find(strcmp(predicted(a),prior)));
    order(a,1:k) = find(strcmp(predicted(a),prior));
    index(a,1:k) = find(strcmp(predicted(a),prior));
end
end