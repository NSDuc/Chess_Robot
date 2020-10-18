%clear;clc;
%clearvars -except s; clc;
%x = 266; y = 285;
    x = 464; y = 884;
    robotX = 501; robotY = -183;
    pxldis = 0.0312;
    d = pxldis * sqrt((x-501)^2 + (y-(-183))^2);
    
    degree = atand((y-robotY) / (robotX-x));
    if degree < 0
        degree = 180 + degree;
    end
    j11 = fix(degree * 19.4);
    
    h = 4;%3.8
    if d < 20
        df36 = d - 16;
    elseif d < 30
        df36 = d - 17;
    else
        df36 = d - 17.5;
    end
    if df36 < 0
        j366 = fix(asind(df36 / 18) / 0.086);
        j366 = round(j366 * 1.4);
    else
        j366 = fix(asind(df36 / 18) / 0.086);
    end
    
    if j366 < -100
        h36 = -0.1*(j366+100)/50;
    elseif j366 < -50
        h36 = -0.1 + (-(0.1*(j366+50)/50));
    elseif j366 < 0
        h36 = 0.1*j366/50;
    elseif j366 <= 50
        h36 = 0.1*j366/50;
    elseif j366 <= 100
        h36 = 0.1 + 0.2*(j366-50)/50;
    elseif j366 <= 150
        h36 = 0.3 + 0.35*(j366-100)/50;
    elseif j366 <= 200
        h36 = 0.65 + 0.45*(j366-150)/50;
    elseif j366 <= 300
        h36 = 1.1 + 0.55*(j366-200)/50;
    elseif j366 <= 400
        h36 = 2.2 + 0.75*(j366-300)/50;
    elseif j366 <= 450
        h36 = 3.7 + 0.8*(j366-400)/50;
    elseif j366 <= 1000
        h36 = 4.5 + 0.95*(j366-450)/50;
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
            j22 = j2tp;
            break;
        end
    end
    fh = h - h2;

%------------------------------------
% x=450 y=880 j1=1692 j36=700 j2=900
a36 = 700;
a2 = 900;
a36d = 18 * sind(0.86 * a36/10);
a2d = 18 * cosd(34.8 - 0.51 * a2/10);
%di = a36d + a2d; 700 900

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