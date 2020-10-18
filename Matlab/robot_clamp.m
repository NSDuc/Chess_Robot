function [currentj1,currentj36] =robot_clamp(s,cj1,cj2,cj36,cj45r,currentj1,currentj36)
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
        if j1 > 2000
           u = 0.5*(round((j1-2000),-1)/100);
           pause(u);
        else
            pause(0.3);
        end
    end
    clear q;
    q = fread(s);
    %pause(0.1)
    if q(end-1:end) == [49;13]
        
        continue;
    else
        break;
    end
    
end
currentj1 = cj1;
currentj36 = cj36;
end
%}