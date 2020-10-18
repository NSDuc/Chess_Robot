clearvars -except s; clc;
load prior.mat
load test.mat
%{
if exist('s') == 0
    s = serial('COM1','BaudRate',9600,'DataBits', 8,'Terminator','CR');
    fopen(s);
end
%}
a = [3 1 25 5 8 26 28 24 2 4 6 17 30 27 13 23 9 7 10 20 29 12 14 21 22 11 15 16 18 19]';%7 10 20 29 back
b = [1 2 3 4 5 6 7 9 11 12 13 14 16 17 18 19 21 8 20 22 15 24 26 28 27 29 31 33 32 30]';
currentj1 = 0;
currentj36 = 0;
%[currentj1,currentj36] =robot_clamp2(s,chess(sortidx(j),1),chess(sortidx(j),2),chess(sortidx(j),3),chess(sortidx(j),5),currentj1,currentj36);
%[currentj1,currentj36] =robot_turn_2(s,currentj1,currentj36);
%[currentj1,currentj36] =robot_turn2_2(s,currentj1,currentj36);
%[currentj1,currentj36,check] =robot_place2(s,robo_tag(j,1),robo_tag(j,2),robo_tag(j,3),robo_tag(j,4),robo_tag(j,5),currentj1,currentj36);
prior2 = str2double(prior(1:22,4:8));
prior2(24:33,:) = str2double(prior(24:33,4:8));

for j = 1:30
    [currentj1,currentj36] =robot_clamp2(s,test(a(j),1),test(a(j),2),test(a(j),3),test(a(j),5),currentj1,currentj36);
    
    if j == 18||j == 19||j == 20||j == 21
        [currentj1,currentj36] =robot_turn_2(s,currentj1,currentj36);
        pause(2)
        [currentj1,currentj36] =robot_turn2_2(s,currentj1,currentj36);
    end
    
    [currentj1,currentj36,~] =robot_place2(s,prior2(b(j),1),prior2(b(j),2),prior2(b(j),3),prior2(b(j),4),prior2(b(j),5),currentj1,currentj36);

end
%}