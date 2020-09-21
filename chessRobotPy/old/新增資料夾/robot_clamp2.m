function [currentj1,currentj36] =robot_clamp2(s,cj1,cj2,cj36,cj45r,currentj1,currentj36)
j1 = cj1 - currentj1;
j2 = cj2;
j36 = cj36 - currentj36;
j45 = cj45r;
%---------------------------robot action-------------------------------------
joint1_chs = ['@STEP 221,',num2str(j1),',0,0,0,0,0,0'];
joint2_chs = ['@STEP 221,0,',num2str(j2),',0,0,0,0,0'];
joint2_chsi = ['@STEP 221,0,',num2str(-j2),',0,0,0,0,0'];
joint36_chs = ['@STEP 221,0,0,',num2str(j36),',0,0,',num2str(j36),',0'];
joint45_chs = ['@STEP 221,0,0,0,',num2str(j45),',',num2str(-j45),',0,0'];
joint45_chsi = ['@STEP 221,0,0,0,',num2str(-j45),',',num2str(j45),',0,0'];
%joint36_chsi = ['@STEP 221,0,0,',num2str(-j36),',0,0,',num2str(-j36),',0'];
%gp_op = ['@STEP 221,0,0,0,0,0,110,0'];
gp_cl = ['@STEP 221,0,0,0,0,0,-110,0'];
%---------------------------robot run-------------------------------------
for k = 1:7
    if k == 1
        fprintf(s,joint1_chs);
    elseif k == 2
        fprintf(s,joint36_chs);
    elseif k == 3
        fprintf(s,joint45_chs);
    elseif k == 4
        fprintf(s,joint2_chs);
    elseif k == 5
        fprintf(s,gp_cl);
    elseif k == 6
        fprintf(s,joint2_chsi);
    else
        fprintf(s,joint45_chsi);
    end
    %--------------------------
    if k == 1
        if j1 < 1000
            pause(5.5);
        else
            u1 = 0.5*(round((j1-1000),-1)/100) + 5.5;
            pause(u1);
        end
    elseif k == 2
        if (-j36) <= 200
            pause(2);
        else
            u2 = 0.5*(round((-j36-200),-1)/100) + 2;
            pause(u2);
        end
    elseif k == 3
        if abs(j45) <= 150
            pause(1.5);
        else
            u4 = 0.3*(round((abs(j45)-150),-1)/50) + 1.5;
            pause(u4);
        end
    elseif k == 4
        if j2 <= 250
            pause(2.5);
        else
            u4 = 1*(round((j2-250),-1)/250) + 2.5;
            pause(u4);
        end
    elseif k == 6
        if j2 <= 250
            pause(2.5);
        else
            u6 = 1*(round((j2-250),-1)/250) + 2.5;
            pause(u6);
        end
    elseif k == 7
        if abs(j45) <= 150
            pause(1.5);
        else
            u4 = 0.3*(round((abs(j45)-150),-1)/50) + 1.5;
            pause(u4);
        end
    else
        pause(1.5);
    end
end
currentj1 = cj1;
currentj36 = cj36;
end
%}