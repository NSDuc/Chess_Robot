import numpy as np

def calcu_position(predicted,posX,posY):
    load chesslocation.mat
    L = size(posX,1);
    for i in range(0:L):
        x = posX(i); y = posY(i);
        camposi_x = 682.3; camposi_y = 494.7; camposi_xh = 1508; camposi_yh = 1509;
        chess_h = 32.05;
        x = round(x +((chess_h * (camposi_x - x)) / camposi_xh),1);
        y = round(y +((chess_h * (camposi_y - y)) / camposi_yh),1);
        src = np.array([x,y,1]).T;
        thx = 180;
        rotx = np.array([1 0 0;0 cosd(thx) -sind(thx);0 sind(thx) cosd(thx)]);
        thz = 180.3;
        rotz = np.array([np.cosd(thz), -np.sind(thz), 0; np.sind(thz), np.cosd(thz), 0; 0,0,1]);
        scale = np.array([1 0 0;0 1 0;0 0 1])
        tran = np.array([1 0 -475;0 1 187;0 0 1])
        #---------------------------------------------
        new(i,:) = (round((rotx * rotz * scale * tran * src),2)).T;
        nxy(i,:) = new(i,1:2);
        rx = nxy(i,1); ry = nxy(i,2);
        degree = atan2d(ry,rx);
        j1(i) = round(degree * 19.64);
        #--------------------------------------------
        
        new1 = new
        nxy1 = nxy
        rx1  = nxy1[0,0]; ry1 = nxy1[0,1]
        
        srctheta2 = 41.3;
        %-------------
        srctheta3 = -89;
        %--------------
        pxldis = 0.0312;
        d = np.around(pxldis * np.sqrt(rx1**2 + ry1**2));
        d_src = d;
        
            
        if (d > 34.5):
            d = 34.5;
            d_dif = d_src(i) - d;
            j45_theta = np.asind(d_dif/9.2);
            j45[i] = np.around(-j45_theta * 4.27);
            j45_rotate[i] = 0;
        else:
            j45[i] = 0;
            j45_rotate[i] = np.around((degree-90) * 4.27);
            if abs(j45_rotate[i]) < 15:
                j45_rotate[i] = 0
        
        p = np.sqrt(8.54^2 +d^2);
        theta_a = np.atand(8.55 / d);
        theta_b = np.acosd((17.78**2 + 17.78**2 - p**2) / (2*17.78*17.78));
        theta_c = (180 - theta_b) / 2;
        theta_3 = -(theta_a + theta_c);
        theta_2 = 180 - theta_a - theta_b - theta_c;
        
        j36[i] = np.around(-(theta_3 - srctheta3)* 11.55);
        j2[i]  = np.around(-(theta_2 - srctheta2)* 19.64);

    currentj1 = 0;
    currentj36 = 0;
    chess = np.array([j1.T, j2.T, j36.T, j45.T, j45_rotate.T])
    b = [7 9 5 3 1 2 4 8 6 23 25 21 19 17 18 20 24 22 11 10 27 26 33 16 12 15 13 14 32 28 31 29 30];
    for p in range(0:33):
        prior(p,:) = chesslocation(b[p],:);
    order = np.zeros(L[0],5);
    for a in range(0:L):
        k = size(find(strcmp(predicted(a),prior)));
        order[a,1:k] = find(strcmp(predicted(a),prior));
        index[a,1:k] = find(strcmp(predicted(a),prior));

    return chess,order,index,prior