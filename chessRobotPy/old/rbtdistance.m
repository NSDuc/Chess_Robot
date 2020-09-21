%clear;clc;
%x = 266; y = 285;
L = size(center,1);
for i = 1:L
    x = center(i,1); y = center(i,2);
    robotX = 501; robotY = -183;
    pxldis = 0.0312;
    d = pxldis * sqrt((x-501)^2 + (y-(-183))^2);
    
    degree = atand((y-robotY) / (robotX-x));
    if degree < 0
        degree = 180 + degree;
    end
    j1(:,i) = fix(degree * 19.4);
    
    h = 4;
    
    if d < 20
        df36 = d - 16;
    elseif d < 30
        df36 = d - 17;
    else
        df36 = d - 17.5;
    end
    j36(:,i) = fix(asind(df36 / 18) / 0.086);
    
    if j36(:,i) <= 50
        h36 = 0.1*j36(:,i)/50;
    elseif j36(:,i) <= 100
        h36 = 0.1 + 0.2*(j36(:,i)-50)/50;
    elseif j36(:,i) <= 150
        h36 = 0.3 + 0.35*(j36(:,i)-100)/50;
    elseif j36(:,i) <= 200
        h36 = 0.65 + 0.45*(j36(:,i)-150)/50;
    elseif j36(:,i) <= 300
        h36 = 1.1 + 0.55*(j36(:,i)-200)/50;
    elseif j36(:,i) <= 400
        h36 = 2.2 + 0.75*(j36(:,i)-300)/50;
    elseif j36(:,i) <= 450
        h36 = 3.7 + 0.8*(j36(:,i)-400)/50;
    elseif j36(:,i) <= 1000
        h36 = 4.5 + 0.95*(j36(:,i)-450)/50;
    end
    h = h + h36;
    if h > 2.3
        j2tp = 150;
    elseif h > 5.2
        j2tp = 350;
    end
    while 1
        if j2tp <= 150
            h2 = 0.6 * j2tp/50;
        elseif j2tp <= 350
            h2 = 1.8 + 0.7*(j2tp-150)/50;
        elseif j2tp <= 1000
            h2 = 4.6 + 0.75*(j2tp-350)/50;
        else
            break;
        end
        if (h - h2) < 0.4
            while 1
                j2tp = j2tp - 1;
                if ~(rem(j2tp,10) ~= 0)
                    break;
                end
            end
        elseif (h - h2) > 0.65
            while 1
                j2tp = j2tp + 1;
                if ~(rem(j2tp,10) ~= 0)
                    break;
                end
            end
        else
            j2(:,i) = j2tp;
            break;
        end
    end
    fh = h - h2;
end
%------------------------------------
%a36 = [215 225];
%a2 = 170;
%a36d = 18 * sind(0.86 * a36/10);
%a2d = 18 * cosd(34.8 - 0.51 * a2/10);
%di = a36d + a2d;

%t2 = 180;
%{
if t2 <= 150
    ht2 = 0.6 * t2/50;
elseif t2 <= 350
    ht2 = 1.8 + 0.7*(t2-150)/50;
elseif t2 <= 500
    ht2 = 4.6 + 0.75*(t2-350)/50;
end
%}
%[x,y] = solve('0.0312*sqrt((x-266)^2 + (y-285)^2) = 16.557',...
%   '0.0312*sqrt((x-688)^2 + (y-379)^2) = 18.317','x,y');
%x1 = double(x);
%y1 = double(y);
%{
p = 501;
t = -183;
a = 0.0312 * sqrt((p-266)^2+(t-285)^2);
%}