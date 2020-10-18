load chesslocation.mat
L = size(posX);
%L = 32;
for i = 1:L
    x = posX; y = posY;
    %x = chesslocation(:,2); y = chesslocation(:,3);
    %x = str2double(x); y = str2double(y);
    robotX = 501; robotY = -213;
    srctheta2 = 43; srctheta3 = -85;
    pxldis = 0.0312;
    d = pxldis * sqrt((x(i)-robotX)^2 + (y(i)-robotY)^2);
    d_src  = d;
    if d > 34.5
        d = 34.5;
        d_dif = d_src - d;
        j45(:,i) = fix(-d_dif * 25);
    else
        j45(:,i) = 0;
    end
    
    if x(i) < 501
        rj1X = 501; rj1Y = -163;
    else
        rj1X = 501; rj1Y = -213;
    end
    degree = atand((y(i)-rj1Y) / (rj1X-x(i)));
    if degree < 0
        degree = 180 + degree;
    end
    j1(:,i) = fix(degree * 19.5);
    
    p = sqrt(8.55^2 +d^2);
    theta_a = atand(8.55 / d);
    theta_b = acosd((17.78^2 + 17.78^2 - p^2) / (2*17.78*17.78));
    theta_c = (180 - theta_b) / 2;
    theta_3 = -(theta_a + theta_c);
    theta_2 = 180 - theta_a - theta_b - theta_c;
    
    j36(:,i) = fix(-(theta_3 - srctheta3)* 11.765);
    j2(:,i) = fix(-(theta_2 - srctheta2) * 19.5);
end

current = 0;
chess = [j1' j2' j36' j45'];
%{
for j = 1:2
    target_pre =find(strcmp(predicted(j),chesslocation));
    target_check = find(strcmp(chesslocation(target_pre,9),"0"));
    target = target_pre(target_check(1));
    robot_target = str2double(chesslocation(target,4:8));
    
    chessj1 = chess(j) - current;
    targetj1 = robot_target(1) - chess(j);
    
    current = robot_target(1);
end
%}
%{
    %---------------------------robot action-------------------------------------
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
        
    gp_op = ['@STEP 221,0,0,0,0,0,125,0'];
    gp_cl = ['@STEP 221,0,0,0,0,0,-125,0'];
    %---------------------------robot run-------------------------------------
    
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
            chesslocation(target,9) = "1";
        end
        
        clear q;
        q = fread(s);
        if q(end-1:end) == [49;13]
            continue;
        else
            break;
        end
        
    end
    if j == L(1)
        initialization = ['@STEP 221,',num2str(-robot_target(1)),',0,0,0,0,0,0'];
        fprintf(s,initialization);
    end
    
end
%}