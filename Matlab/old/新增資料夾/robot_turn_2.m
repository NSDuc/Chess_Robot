function [currentj1,currentj36] =robot_turn_2(s,currentj1,currentj36)
j1 = -(currentj1 - 900);
j36 = -(currentj36 + 400);
%---------------------------robot action-------------------------------------
turnj1 = ['@STEP 221,',num2str(j1),',0,0,0,0,0,0'];
recoj1 = ['@STEP 221,1050,0,0,0,0,0,0'];

turnj2 = ['@STEP 221,0,510,0,0,0,0,0'];
turnj2i = ['@STEP 221,0,-510,0,0,0,0,0'];
recoj2 = ['@STEP 221,0,700,0,0,0,0,0'];
recoj2i = ['@STEP 221,0,-700,0,0,0,0,0'];

oj36 = ['@STEP 221,0,0,',num2str(j36),',0,0,',num2str(j36),',0'];
turnj36i = ['@STEP 221,0,0,380,0,0,380,0'];

turnj45 = ['@STEP 221,0,0,0,-340,-340,0,0'];
rotaj45 = ['@STEP 221,0,0,0,-770,770,0,0'];

gp_op = ['@STEP 221,0,0,0,0,0,110,0'];
gp_cl = ['@STEP 221,0,0,0,0,0,-110,0'];

%---------------------------robot run-------------------------------------

for k = 1:16
    if k == 1
        fprintf(s,turnj1);
    elseif k == 2
        fprintf(s,oj36);
    elseif k == 3
        fprintf(s,turnj2);
        pause(3.5);
    elseif k == 4
        fprintf(s,gp_op);
        pause(1.5);
    elseif k == 5
        fprintf(s,turnj2i);
        pause(3.5);
    elseif k == 6
        fprintf(s,turnj36i);
        pause(3);
    elseif k == 7
        fprintf(s,turnj45);
        pause(2.5);
    elseif k == 8
        fprintf(s,recoj2);
        pause(4.5);
    elseif k == 9
        fprintf(s,gp_cl);
        pause(1.5);
    elseif k == 10
        fprintf(s,recoj2i);
        pause(4.5);
    elseif k == 11
        fprintf(s,rotaj45);
        pause(4.5);
    elseif k == 12
        fprintf(s,recoj2);
        pause(4.5);
    elseif k == 13
        fprintf(s,gp_op);
        pause(1.5);
    elseif k == 14
        fprintf(s,gp_cl);
        pause(1.5);
    elseif k == 15
        fprintf(s,recoj2i);
        pause(4.5);
    else
        fprintf(s,recoj1);
        pause(6);
    end
    %------------------------------------
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
    end
end
currentj1 = 1050;
currentj36 = -20;
end
%}