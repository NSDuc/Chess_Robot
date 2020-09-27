import numpy as np

def main:
    my_posX = np.array([52 , 283, 405, 546]).T
    my_posY = np.array([102, 249, 579, 462]).T

    calcu_position (0, my_posX, my_posY)

def calcu_position(predicted,posX,posY):
    import chesslocation.py
    L = np.shape(posX)[0]
    new = np.zeros((L, 3))
    j1 = np.zeros(L).T
    j2 = np.zeros(L).T
    j36 = np.zeros(L).T
    j45 = np.zeros(L).T
    j45_rotate = np.zeros(L).T
    for i in range(L):
        x = posX[i]
        y = posY[i]
        camposi_x = 682.3
        camposi_y = 494.7
        camposi_xh = 1508
        camposi_yh = 1509
        chess_h = 32.05
        x = round(x +((chess_h * (camposi_x - x)) / camposi_xh),1)
        y = round(y +((chess_h * (camposi_y - y)) / camposi_yh),1)
        src = np.array([x, y, 1]).T
        thx = 180
        rotx = np.array([[1, 0, 0],
                         [0, np.cos(np.deg2rad(thx)), -np.sin(np.deg2rad(thx))],
                         [0, np.sin(np.deg2rad(thx)), np.cos(np.deg2rad(thx))]])
        thz = 180.3
        rotz = np.array([[np.cos(np.deg2rad(thz)), -np.sin(np.deg2rad(thz)), 0],
                         [np.sin(np.deg2rad(thz)), np.cos(np.deg2rad(thz)), 0],
                         [0, 0, 1]])
        scale = np.eye(3, dtype=float)
        tran  = np.array([[1, 0, -475], [0, 1, 187], [0, 0, 1]])
        new[i,:] = np.around((rotx @ rotz @ tran @ scale @ src),2).T.copy()
        nxy = new[i,0:2].copy()
        rx = nxy[i,0]
        ry = nxy[i,1]
        degree = np.rad2deg(np.arctan2(ry,rx))
        j1[i] = np.around(degree * 19.64)
        
        new1 = new.copy()
        nxy1 = nxy.copy()
        rx1  = nxy1[0,0]
        ry1  = nxy1[0,1]
        
        srctheta2 = 41.3
        srctheta3 = -89
        pxldis = 0.0312
        d = np.around(pxldis * np.sqrt(rx1**2 + ry1**2),2)
        d_src = d.copy()
        
            
        if d > 34.5:
            d = 34.5
            d_dif = d_src[i] - d
            j45_theta = np.rad2deg(np.asin(d_dif/9.2))
            j45[i] = np.around(-j45_theta * 4.27)
        else:
            j45_rotate[i] = np.around((degree - 90) * 4.27)
            if abs(j45_rotate[i]) < 15:
                j45_rotate[i] = 0
        
        p = np.sqrt(8.54**2 +d**2)
        theta_a = np.rad2deg(np.arctan(8.55 / d))
        theta_b = np.rad2deg(np.arccos((17.78**2 + 17.78**2 - p**2) / (2 * 17.78 * 17.78)))
        theta_c = (180 - theta_b) / 2
        theta_3 = -(theta_a + theta_c)
        theta_2 = 180 - theta_a - theta_b - theta_c
        
        j36[i] = np.around(-(theta_3 - srctheta3) * 11.55)
        j2[i]  = np.around(-(theta_2 - srctheta2) * 19.64)

    currentj1  = 0
    currentj36 = 0
    prior = np.zeros((33,6))
    chess = np.array([j1.T, j2.T, j36.T, j45.T, j45_rotate.T])
    b = [7 , 9 , 5 , 3 , 1 , 2 , 4 , 8 , 6 , 23, 25,
         21, 19, 17, 18, 20, 24, 22, 11, 10, 27, 26,
         33, 16, 12, 15, 13, 14, 32, 28, 31, 29, 30];
    # for p in range(33):
    #     prior[p,:] = chesslocation.chesslocation((b[p] - 1),:);
    # order = np.zeros((L,5));
    # for a in range(L):
    #     k = size(find(strcmp(predicted(a),prior)));
    #     order[a,0:k] = find(strcmp(predicted(a),prior));
    #     index[a,0:k] = find(strcmp(predicted(a),prior));

    return chess, order, index, prior