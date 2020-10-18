function [currentj1,currentj36] =robot_reset(s.currentj1,currentj36)
j1 = - currentj1;
j36 = - currentj36;

joint1_o = ['@STEP 221,',num2str(j1),',0,0,0,0,0,0'];
joint36_o = ['@STEP 221,0,0,',num2str(j36),',0,0,',num2str(j36),',0'];

for k = 1:2
    if k == 1
        fprintf(s,joint1_o);
    else
        fprintf(s,joint36_o);
    end
    clear q;
    q = fread(s);
    if q(end-1:end) == [49;13]
        continue;
    else
        break;
    end
end
currentj1 = 0;
currentj36 = 0;
end