clearvars -except s; clc;
load chesslocation.mat
%srcx = 437; srcy = 325; %72.65 544.33
%srcx = 527; srcy = 613; %-13.97 826.68
srcx = 757; srcy = 444; %-239.93 662.47

%for i = 2
%srcx = test(i,1); srcy = test(i,2);
camposi_x = 682.3; camposi_y = 494.7; camposi_xh = 1508; camposi_yh = 1509;
%camposi_x = 700; camposi_y = 440; camposi_xh = 1500; camposi_yh = 1500;
chess_h = 32.05;
x = round(srcx +((chess_h * (camposi_x - srcx)) / camposi_xh),1);
y = round(srcy +((chess_h * (camposi_y - srcy)) / camposi_yh),1);
%end
%x = srcx; y = srcy;

src = [x,y,1]';
thx = 180;
rotx = [1 0 0;0 cosd(thx) -sind(thx);0 sind(thx) cosd(thx)];
thz = 180.3;
rotz = [cosd(thz) -sind(thz) 0;sind(thz) cosd(thz) 0;0 0 1];
scale = [1 0 0;0 1 0;0 0 1];%1 1.0135
tran = [1 0 -512;0 1 216.1;0 0 1];%-489 196
%{
if x <= 490
    thz = 181; %181.1
    rotz = [cosd(thz) -sind(thz) 0;sind(thz) cosd(thz) 0;0 0 1];
    scale = [1 0 0;0 1 0;0 0 1];%1.0418
    tran = [1 0 -475;0 1 187;0 0 1];%-485 208 218

else
    thz = 181; %180.3
    rotz = [cosd(thz) -sind(thz) 0;sind(thz) cosd(thz) 0;0 0 1];
    scale = [1 0 0;0 1 0;0 0 1];%1.024
    tran = [1 0 -475;0 1 187;0 0 1];%-495 190
end
%}
new = (round((rotx * rotz * tran * scale * src),2))';
nxy = new(1,1:2);

rx = nxy(1,1); ry = nxy(1,2);
degree = atan2d(ry,rx);
%{
%degree = atand(ry / rx);

if degree < 0
    degree = 180 + degree;
end
%}
j1 = round(degree * 19.64);
%------------------------------------------
%{
if x <= 494
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
%}
new1 = new;
nxy1 = nxy;
%new1 = (round((rotx * rotz * tran * scale * src),2))';
%nxy1 = new1(1,1:2);
rx1 = nxy1(1,1); ry1 = nxy1(1,2);

%srctheta2 = 42.7; 
%srctheta2 = 41.3;
srctheta2 = 38; 
%srctheta3 = -85;
srctheta3 = -86.6;
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

j36 = round(-(theta_3 - srctheta3)* 11.55); %11.765
j2 = round(-(theta_2 - srctheta2) * 19.64); %19.5
%}

z = [j1' j2' j36' j45' j45_rotate'];
%current = 0;
%chess = [j1' j2' j36' j45'];
%{
current = 0;
chess = [j1' j2' j36' j45'];

target_pre =find(strcmp(predicted(j),chesslocation));
target_check = find(strcmp(chesslocation(target_pre,8),"0"));
target = target_pre(target_check(1));
robot_target = str2double(chesslocation(target,4:7));

chessj1 = chess(j) - current;
targetj1 = robot_target(1) - chess(j);

current = robot_target(1);

%origin = ['@STEP 221,',num2str(-robot_target(1)),',0,0,0,0,0,0'];
j = 1;
joint1_chs = ['@STEP 221,',num2str(chessj1),',0,0,0,0,0,0'];
joint1_tag = ['@STEP 221,',num2str(targetj1),',0,0,0,0,0,0'];

joint2_chs = ['@STEP 221,0,',num2str(chess(j,2)),',0,0,0,0,0'];
joint2_chsi = ['@STEP 221,0,',num2str(-chess(j,2)),',0,0,0,0,0'];
joint36_chs = ['@STEP 221,0,0,',num2str(chess(j,3)),',0,0,',num2str(chess(j,3)),',0'];
joint36_chsi = ['@STEP 221,0,0,',num2str(-chess(j,3)),',0,0,',num2str(-chess(j,3)),',0'];
%joint45_chs = ['@STEP 221,0,0,0,',num2str(chess(j,4)),',',num2str(chess(j,4)),',0,0'];
%joint45_chsi = ['@STEP 221,0,0,0,',num2str(-chess(j,4)),',',num2str(-chess(j,4)),',0,0'];

joint2_tag = ['@STEP 221,0,',num2str(robot_target(2)),',0,0,0,0,0'];
joint2_tagi = ['@STEP 221,0,',num2str(-robot_target(2)),',0,0,0,0,0'];
joint36_tag = ['@STEP 221,0,0,',num2str(robot_target(3)),',0,0,',num2str(robot_target(3)),',0'];
joint36_tagi = ['@STEP 221,0,0,',num2str(-robot_target(3)),',0,0,',num2str(-robot_target(3)),',0'];
joint45_tag = ['@STEP 221,0,0,0,',num2str(robot_target(4)),',',num2str(robot_target(4)),',0,0'];
joint45_tagi = ['@STEP 221,0,0,0,',num2str(-robot_target(4)),',',num2str(-robot_target(4)),',0,0'];

gp_op = ['@STEP 221,0,0,0,0,0,120,0'];
gp_cl = ['@STEP 221,0,0,0,0,0,-120,0'];
gp_on = ['@STEP 221,0,0,0,0,0,450,0'];
gp_off = ['@STEP 221,0,0,0,0,0,-450,0'];
%---------------------------------------------------------------------------------

for k = 1:14
    if k == 1
        fprintf(s,joint1_chs);
    elseif k == 2
        fprintf(s,joint36_chs);
    elseif k == 3
        fprintf(s,joint2_chs);
    elseif k == 4
        fprintf(s,gp_cl);
    elseif k == 5
        fprintf(s,joint2_chsi);
    elseif k == 6
        fprintf(s,joint36_chsi);
    elseif k == 7
        fprintf(s,joint1_tag);
    elseif k == 8
        fprintf(s,joint36_tag);
    elseif k == 9
        fprintf(s,joint45_tag);
    elseif k == 10
        fprintf(s,joint2_tag);
    elseif k == 11
        fprintf(s,gp_op);
    elseif k == 12
        fprintf(s,joint2_tagi);
    elseif k == 13
        fprintf(s,joint45_tagi);
    else
        fprintf(s,joint36_tagi);
        chesslocation(target,8) = "1";
    end
    clear q;
    q = fread(s);
    if q(end-1:end) == [49;13]
        continue;
    else
        break;
    end
    
end
%}