import numpy as np

def calcu_position(predicted,posX,posY):
    #global chesslocation
    #load chesslocation.mat
    L = posX.shape[0]
    for i in range(0,L):
        x = posX[i]
        y = posY[i]
        camposi_x = 682.3; camposi_y = 494.7; camposi_xh = 1508; camposi_yh = 1509;
        chess_h = 32.05
        x = np.around(x +((chess_h * (camposi_x - x)) / camposi_xh),1)
        y = np.around(y +((chess_h * (camposi_y - y)) / camposi_yh),1)
        src = np.array([x,y,1]).T
        thx = 180
        thxrad = np.deg2rad(thx)
        rotx = np.array([[1,0,0],
            [0,np.cos(thxrad),-np.sin(thxrad)],
            [0,np.sin(thxrad),np.cos(thxrad)]])

        thz = 180.3;
        thzrad = np.deg2rad(thz)
        rotz = np.array([[np.cos(thzrad),-np.sin(thzrad),0],
            [np.sin(thzrad),np.cos(thzrad),0],
            [0,0,1]])
        
        scale = np.array([[1 0 0], [0 1 0], [0 0 1]])
        tran = np.array([[1 0 -475],[0 1 187], [0 0 1]])
        #---------------------------------------------
        new[i:] = np.around((rotx * rotz * scale * tran * src),2).T;
        nxy[i:] = new[i,1:2]
        rx = nxy[i,1]
        ry = nxy[i,2]
        degree = np.rad2deg(np.arctan2(ry,rx))
        j1[i] = np.round(degree * 19.64);
        #--------------------------------------------
        
        new1 = new
        nxy1 = nxy
        rx1  = nxy1[0,0]; ry1 = nxy1[0,1]
        
        srctheta2 = 41.3;
        srctheta3 = -89;
        pxldis = 0.0312;
        d = np.around((pxldis * np.sqrt(rx1**2 + ry1**2)), 2)
        d_src = d;
        
            
        if (d > 34.5):
            d = 34.5
            d_dif = d_src[i] - d;
            j45_theta = np.arcsin(np.deg2rad(d_dif/9.2))
            j45[i] = np.around(-j45_theta * 4.27);
            j45_rotate[i] = 0;
        else:
            j45[i] = 0;
            j45_rotate[i] = np.around((degree-90) * 4.27)
            if abs(j45_rotate[i]) < 15:
                j45_rotate[i] = 0
        
        p = np.sqrt(8.54^2 +d^2);
        theta_a = np.arctan(np.deg2rad(8.55 / d))
        theta_b = np.arccos(np.deg2rad((17.78**2 + 17.78**2 - p**2) / (2*17.78*17.78)))
        theta_c = (180 - theta_b) / 2;
        theta_3 = -(theta_a + theta_c);
        theta_2 = 180 - theta_a - theta_b - theta_c;
        
        j36[i] = np.around(-(theta_3 - srctheta3)* 11.55);
        j2[i]  = np.around(-(theta_2 - srctheta2)* 19.64);

    currentj1 = 0;
    currentj36 = 0;
    chess = np.array([j1.T, j2.T, j36.T, j45.T, j45_rotate.T])
    b = np.array([7 9 5 3 1 2 4 8 6 23 25 21 19 17 18 20 24 22 11 10 27 26 33 16 12 15 13 14 32 28 31 29 30])
    for p in range(0,32):
        prior[p,:] = chesslocation(b[p],:)
    order = np.zeros((L[0],5))
    for a in range(0,L):
        k = np.where(predicted[a] == prior).shape[]
        order[a,0:k] = np.where(predicted[a] == prior)
        index[a,0:k] = np.where(predicted[a] == prior)

    return chess,order,index,prior