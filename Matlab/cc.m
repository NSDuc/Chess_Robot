clearvars -except s; clc;


j1 = 1618;
j2 = 140;
j36 = -45;
j45 = -0;

theta_1 = j1 / 19.64;
theta_2 = -j2 / 19.64 + 42.7;
theta_3 = -j36 / 11.55 - 85;
theta_4 = -j45 / 4.27 - 90;
d = round(17.78*cosd(theta_2) + 17.78*cosd(theta_3) + 9.2*cosd(theta_4),2);
h = 17.78*sind(theta_2) + 17.78*sind(theta_3) + 9.2*sind(theta_4);
pixd = d / 0.0312;
rx = pixd*cosd(theta_1);
ry = pixd*sind(theta_1);
%}
%{
thx = 180;
rotx = [1 0 0;0 cosd(thx) -sind(thx);0 sind(thx) cosd(thx)];
thz = 90;
rotz = [cosd(thz) -sind(thz) 0;sind(thz) cosd(thz) 0;0 0 1];
tran = [1 0 -3;0 1 0;0 0 1];
scale = [1.0361 0 0;0 1 0;0 0 1];
x1 = rotx * rotz;% * scale * tran;
x2 = x1 * [2;3;1]
%}