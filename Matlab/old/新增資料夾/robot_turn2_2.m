function [currentj1,currentj36] =robot_turn2_2(s,currentj1,currentj36)
%---------------------------robot action-------------------------------------
recoj1i = ['@STEP 221,-1050,0,0,0,0,0,0'];

recoj2 = ['@STEP 221,0,700,0,0,0,0,0'];
recoj2i = ['@STEP 221,0,-700,0,0,0,0,0'];
turnj22 = ['@STEP 221,0,520,0,0,0,0,0'];
turnj22i = ['@STEP 221,0,-520,0,0,0,0,0'];

turnj366 = ['@STEP 221,0,0,-390,0,0,-390,0'];

turnj45i = ['@STEP 221,0,0,0,340,340,0,0'];
rotaj45i = ['@STEP 221,0,0,0,770,-770,0,0'];

gp_op = ['@STEP 221,0,0,0,0,0,110,0'];
gp_cl = ['@STEP 221,0,0,0,0,0,-110,0'];

%---------------------------robot run-------------------------------------

for k = 1:10
    if k == 1
        fprintf(s,recoj1i);
        pause(6);
    elseif k == 2
        fprintf(s,recoj2);
        pause(4.5);
    elseif k == 3
        fprintf(s,gp_op);
        pause(1.5);
    elseif k == 4
        fprintf(s,recoj2i);
        pause(4.5);
    elseif k == 5
        fprintf(s,rotaj45i);
        pause(4.5);
    elseif k == 6
        fprintf(s,turnj45i);
        pause(2.5);
    elseif k == 7
        fprintf(s,turnj366);
        pause(3);
    elseif k == 8
        fprintf(s,turnj22);
        pause(3.5);
    elseif k == 9
        fprintf(s,gp_cl);
        pause(1.5);
    else
        fprintf(s,turnj22i);
        pause(3.5);
    end
    %-----------------
    
end
currentj1 = 900;
currentj36 = -410;
end
%}