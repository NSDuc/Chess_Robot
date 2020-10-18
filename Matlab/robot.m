%clear;clc%clear parament clc commad
%clearvars -except s; clc;
if exist('s') == 0
    s = serial('COM1','BaudRate',9600,'DataBits', 8,'Terminator','CR');
    %set(s,'BaudRate',9600);fprintf(s,'@STEP 221,100,0,0,0,0,0,0');
    %set(s, 'DataBits', 8);
    %set(s, 'Terminator','CR');
    fopen(s);
end
%gp_on = ['@STEP 221,0,0,0,0,0,430,0'];fprintf(s,gp_on);
%gp_off = ['@STEP 221,0,0,0,0,0,-430,0'];fprintf(s,gp_off);
%gp_op = ['@STEP 221,0,0,0,0,0,110,0'];fprintf(s,gp_op);
%gp_cl = ['@STEP 221,0,0,0,0,0,-110,0'];fprintf(s,gp_cl);

%gp_on = ['@STEP 221,0,0,0,0,0,380,0'];fprintf(s,gp_on);
%gp_off = ['@STEP 221,0,0,0,0,0,-380,0'];fprintf(s,gp_off);
%gp_op = ['@STEP 221,0,0,0,0,0,60,0'];fprintf(s,gp_op);
%gp_cl = ['@STEP 221,0,0,0,0,0,-60,0'];fprintf(s,gp_cl);

%320
%fprintf(s,'@STEP 221,0,0,0,0,0,0,0');
%@STEP <SP>¡AJ1¡AJ2¡AJ3¡AJ4¡AJ5¡AJ6¡A<OUT> 
%B : J1
%S : J2
%E : J3+J6
%P : J4+J5
%R : (°f) -J4+J5,   (¶¶) +J4-J5
%G : J6
%fclose(s); delete(s); clear s;


%fprintf(s,'@STEP 221,2434,0,0,0,0,0,0');
%fprintf(s,'@STEP 221,0,0,0,0,0,0,0');
%g0 = ['@STEP 221,0,0,0,0,0,500,0'];
%m1 = ['@STEP 221,',num2str(j1(1)),',0,0,0,0,0,0'];
%gcl = ['@STEP 221,0,0,0,0,0,-100,0'];
%gop = ['@STEP 221,0,0,0,0,0,100,0'];
%{
if char(predictedLabel) == 'ØX'
    j1 = 1285;
    j2 = 860;
    j36 = 678;
    m1 = ['@STEP 221,',num2str(j1(1)),',0,0,0,0,0,0'];
    m2 = ['@STEP 221,0,0,',num2str(-j36(1)),',0,0,',num2str(-j36(1)),',0'];
    m3 = ['@STEP 221,0,',num2str(j2(1)),',0,0,0,0,0'];
    m4 = '@STEP 221,0,0,0,0,0,-100,0';
    m5 = ['@STEP 221,0,',num2str(-j2(1)),',0,0,0,0,0'];
    m6 = ['@STEP 221,0,0,',num2str(j36(1)),',0,0,',num2str(j36(1)),',0'];
    m7 = ['@STEP 221,',num2str(-j1(1)),',0,0,0,0,0,0'];
    fprintf(s,m1);
    for k = 2:3
        clear q;
        q = fread(s);
        if q(end-1:end) == [49;13]
            eval(['fprintf(s,m',num2str(k),');'])
        end
    end
end
%}
%if char(predictedLabel) == '¨®' 
    %m4 = ['@STEP 221,1400,0,0,0,0,0,0'];
    %m5 = ['@STEP 221,0,0,-450,0,0,-450,0'];
    %m7 = ['@STEP 221,0,0,450,0,0,450,0'];
    %m6 = ['@STEP 221,0,420,0,0,0,0,0'];
    %m8 = ['@STEP 221,0,-420,0,0,0,0,0'];
    %fprintf(s,m5);
    %pause(10);
    %clear q;
    %q = fread(s);
    %if q(end-1:end) == [49;13]
    %fprintf(s,m7);
    %end
%end
%{
if ~isempty(instrfind)
     fclose(instrfind);
      delete(instrfind);
end
%}