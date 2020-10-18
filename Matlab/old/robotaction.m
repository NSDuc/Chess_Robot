%clearvars -except s; clc;
load chesslocation.mat

currentj1 = 0;
currentj36 = 0;
%chess = [j1' j2' j36' j45'];

for j = 1:1
    curt_tag = order(j,find(order(j,:)));
    tag_check = find(strcmp(chesslocation(curt_tag,9),"0"));
    tag = curt_tag(tag_check(1));
    
    [currentj1,currentj36] =robot_clamp(s,chess(j,1),chess(j,2),chess(j,3),currentj1,currentj36);
    if tag == 33
        [currentj1,currentj36] =robot_turn(s,currentj1,currentj36)
        %[tx, ty] = turn_catch(src);
        %predictedLabel(33) = ConvoNN(roi);
        %predicted(L+1) = string(predictedLabel(L+1));
        if exist('roi33') ~= 0
            [currentj1,currentj36] =robot_turn2(s,currentj1,currentj36)
        end
    end
    robo_tag = str2double(chesslocation(tag,4:8));
    [currentj1,currentj36,check] =robot_place(s,robo_tag(j,1),robo_tag(j,2),robo_tag(j,3),...
            robo_tag(j,4),robo_tag(j,5),currentj1,currentj36);
    %}
        
end
%}