clearvars -except s; clc;
load chesslocation.mat
%srcx = 351; srcy = 742;
%srcx = 360; srcy = 220;
%srcx = 913; srcy = 750;
srcx = 924; srcy = 226;

camposi_x = 682.3; camposi_y = 494.7; camposi_xh = 1508; camposi_yh = 1509;
chess_h = 32.05;
x = round(srcx +((chess_h * (camposi_x - srcx)) / camposi_xh),1);
y = round(srcy +((chess_h * (camposi_y - srcy)) / camposi_yh),1);

src = [x,y,1]';
thx = 180;
rotx = [1 0 0;0 cosd(thx) -sind(thx);0 sind(thx) cosd(thx)];
thz = 180.3;
rotz = [cosd(thz) -sind(thz) 0;sind(thz) cosd(thz) 0;0 0 1];
scale = [1 0 0;0 1 0;0 0 1];
tran = [1 0 -479;0 1 191.1;0 0 1];

new = (round((rotx * rotz * tran * scale * src),2))';
nxy = new(1,1:2);

rx = nxy(1,1); ry = nxy(1,2);
degree = atan2d(ry,rx);

j1 = round(degree * 19.64);

new1 = new;
nxy1 = nxy;

rx1 = nxy1(1,1); ry1 = nxy1(1,2);

srctheta2 = 42.7; srctheta3 = -85;
pxldis = 0.0312;
d = round(pxldis * sqrt(rx1^2 + ry1^2),2);
d_src = d;

if d > 34.5
    d = 34.5;
    d_dif = d_src - d;
    j45_theta = asind(d_dif/9.2);
    j45 = round(-j45_theta * 4.27);
    j45_rotate = 0;
else
    j45 = 0;
    j45_rotate = round((degree-90) * 4.27);
end

p = sqrt(8.54^2 +d^2);
theta_a = atand(8.54 / d);
theta_b = acosd((17.78^2 + 17.78^2 - p^2) / (2*17.78*17.78));
theta_c = (180 - theta_b) / 2;
theta_3 = -(theta_a + theta_c);
theta_2 = 180 - theta_a - theta_b - theta_c;

j36 = round(-(theta_3 - srctheta3)* 11.55);
j2 = round(-(theta_2 - srctheta2) * 19.64);

z = [j1' j2' j36' j45' j45_rotate'];