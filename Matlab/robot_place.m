function [currentj1,currentj36,check] =robot_place(s,tj1,tj2,tj36,tj45p,tj45r,currentj1,currentj36)
j1 = tj1 - currentj1;
j2 = tj2;
j36 = tj36 - currentj36;
j45p = tj45p;
j45r = tj45r;
%---------------------------robot action-------------------------------------
joint1_tag = ['@STEP 221,',num2str(j1),',0,0,0,0,0,0'];
joint2_tag = ['@STEP 221,0,',num2str(j2),',0,0,0,0,0'];
joint2_tagsi = ['@STEP 221,0,',num2str(-j2),',0,0,0,0,0'];
joint36_tag = ['@STEP 221,0,0,',num2str(j36),',0,0,',num2str(j36),',0'];
%joint36_tagi = ['@STEP 221,0,0,',num2str(-j36),',0,0,',num2str(-j36),',0'];
joint45p_tag = ['@STEP 221,0,0,0,',num2str(j45p),',',num2str(j45p),',0,0'];
joint45p_tagi = ['@STEP 221,0,0,0,',num2str(-j45p),',',num2str(-j45p),',0,0'];
joint45r_tag = ['@STEP 221,0,0,0,',num2str(j45r),',',num2str(-j45r),',0,0']; %j -100 +100 °f
joint45r_tagi = ['@STEP 221,0,0,0,',num2str(-j45r),',',num2str(j45r),',0,0'];
gp_op = ['@STEP 221,0,0,0,0,0,110,0'];
%gp_cl = ['@STEP 221,0,0,0,0,0,-110,0'];
%---------------------------robot run-------------------------------------

for k = 1:7
    if k == 1
        fprintf(s,joint1_tag);
    elseif k == 2
        fprintf(s,joint36_tag);
    elseif k == 3
        if j45r ~= 0
            fprintf(s,joint45r_tag);
        else
            fprintf(s,joint45p_tag);
        end
    elseif k == 4
        fprintf(s,joint2_tag);
    elseif k == 5
        fprintf(s,gp_op);
    elseif k == 6
        fprintf(s,joint2_tagsi);
    else
        if j45r ~= 0
            fprintf(s,joint45r_tagi);
        else
            fprintf(s,joint45p_tagi);
        end
        check = "1";
    end
    clear q;
    q = fread(s);
    if q(end-1:end) == [49;13]
        continue;
    else
        break;
    end
    
end
currentj1 = tj1;
currentj36 = tj36;
end
%}