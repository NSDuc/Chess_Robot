%load(fullfile('red5.mat'));
load(fullfile('black2.mat'));
roi = im2uint8(roi1);

Q = ConvoNN(roi);

Q = blackpreprocess(Q);
imshow(Q);
%{
load chesslocation.mat
for i = 1:32
    x = chesslocation(i,2); y = chesslocation(i,3);
    x = str2double(x); y = str2double(y);
    %x = posX(i); y = posY(i);
    src = [x,y,1]';
    thx = 180;
    rotx = [1 0 0;0 cosd(thx) -sind(thx);0 sind(thx) cosd(thx)];
        
    if x <= 491
        thz = 180.208; %181.1
        rotz = [cosd(thz) -sind(thz) 0;sind(thz) cosd(thz) 0;0 0 1];
        scale = [1.04 0 0;0 1.011 0;0 0 1];%1.04 1.011
        tran = [1 0 -483.6;0 1 209.6;0 0 1];%-483.6 209.6
    else
        thz = 180.208; %180.3
        rotz = [cosd(thz) -sind(thz) 0;sind(thz) cosd(thz) 0;0 0 1];
        scale = [1.0027 0 0;0 1.0114 0;0 0 1];%1.0027 1.0114
        tran = [1 0 -482.3;0 1 187.3;0 0 1];%-482.3 187.3
    end
    
    %new(i,:) = (round((rotx * rotz * tran * scale * src),2))';
    new(i,:) = (round((rotx * rotz * scale * tran * src),2))';
    nxy(i,:) = new(i,1:2);
    
    rx = nxy(i,1); ry = nxy(i,2);
    srctheta2 = 42.7; srctheta3 = -85;
    pxldis = 0.0312;%0.0312
    d = round(pxldis * sqrt(rx^2 + ry^2),2);
    d_src(i)  = d;
    
    degree = atan2d(ry,rx);
    j1(i) = round(degree * 19.64);
    
    if d > 34.5
        d = 34.5;
        d_dif = d_src(i) - d;
        j45_theta = asind(d_dif/9.2);
        j45(i) = round(-j45_theta * 4.27);
        j45_rotate(i) = 0;
    else
        j45(i) = 0;
        j45_rotate(i) = round((degree-90) * 4.27);
        
    end
    
    p = sqrt(8.54^2 +d^2);
    theta_a = atand(8.55 / d);
    theta_b = acosd((17.78^2 + 17.78^2 - p^2) / (2*17.78*17.78));
    theta_c = (180 - theta_b) / 2;
    theta_3 = -(theta_a + theta_c);
    theta_2 = 180 - theta_a - theta_b - theta_c;
    
    j36(i) = round(-(theta_3 - srctheta3)* 11.55); %11.765
    j2(i) = round(-(theta_2 - srctheta2) * 19.64); %19.5
    
end

z = [j1' j2' j36' j45' j45_rotate'];
%}
%{
for j = 1:32
aa0(j) = sqrt(nxy(j,1)^2 + nxy(j,2)^2);
aa1(j) = sqrt(robo(j,1)^2 + robo(j,2)^2);
end
aa2 = [aa0',aa1'];
%chesslocation2 = chesslocation;
%chesslocation2(:,4:7) = z;
%}

%save('chesslocation.mat', 'chesslocation')