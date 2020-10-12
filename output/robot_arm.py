import numpy as np
import time
import serial

def pause(t):
    #print("pause ", t)
    pass

def robot_place2(tj1 ,tj2 ,tj36 ,tj45p ,tj45r ,currentj1 ,currentj36):
    j1 = tj1 - currentj1
    j2 = tj2
    j36 = tj36 - currentj36
    j45p= tj45p
    j45r= tj45r
    #---------------------------robot action-------------------------------------
    joint1_tag= '@STEP 221,' + str(j1) + ',0,0,0,0,0,0'
    joint2_tag= '@STEP 221,0,' + str(j2) +',0,0,0,0,0'
    joint2_tagsi= '@STEP 221,0,' + str(-j2) + ',0,0,0,0,0'
    joint36_tag= '@STEP 221,0,0,' + str(j36) + ',0,0,' + str(j36) + ',0'
    joint45p_tag= '@STEP 221,0,0,0,' + str(j45p) + ',' + str(j45p) + ',0,0'
    joint45p_tagi= '@STEP 221,0,0,0,' + str(- j45p)+ ',' + str(-j45p) + ',0,0'
    joint45r_tag= '@STEP 221,0,0,0,' + str(j45r) + ',' + str(-j45r) + ',0,0'   
    joint45r_tagi= '@STEP 221,0,0,0,' + str(- j45r) + ',' + str(j45r) + ',0,0'
    gp_op= '@STEP 221,0,0,0,0,0,110,0'
    #---------------------------robot run-------------------------------------
    for k in range(7):
        if k == 0:
            print(joint1_tag)
        elif k == 1:
            print(joint36_tag)
        elif k == 2:
            if j45r != 0:
                print(joint45r_tag)
            else:
                print(joint45p_tag)
        elif k == 3:
            print(joint2_tag)
        elif k == 4:
            print(gp_op)
        elif k == 5:
            print(joint2_tagsi)
        else:
            if j45r != 0:
                print(joint45r_tagi)
            else:
                print(joint45p_tagi)
            check = '1'

        if k == 0:
            if abs(j1) < 1000:
                pause(5.5)
            else:
                u1 = 0.5*(np.round((abs(j1)-1000),-1)/100) + 5.5
                pause(u1)
        elif k == 1:
            if abs(j36) <= 200:
                pause(2)
            else:
                u2 = 0.5*(np.round((abs(j36)-200),-1)/100) + 2
                pause(u2)
        elif k == 2:
            if abs(j45r) <= 150:
                pause(1.5)
            else:
                u4 = 0.3*(np.round((abs(j45r)-150),-1)/50) + 1.5
                pause(u4)
        elif k == 3:
            if j2 <= 250:
                pause(2.5)
            else:
                u4 = 1*(np.round((j2-250),-1)/250) + 2.5
                pause(u4)
        elif k == 5:
            if j2 <= 250:
                pause(2.5)
            else:
                u6 = 1*(np.round((j2-250),-1)/250) + 2.5
                pause(u6)
        elif k == 6:
            if abs(j45r) <= 150:
                pause(1.5)
            else:
                u4 = 0.3*(np.round((abs(j45r)-150),-1)/50) + 1.5
                pause(u4)
        else:
            pause(1.5)
    
    currentj1  = tj1
    currentj36 = tj36
    return currentj1,currentj36,check
    

def robot_clamp2 (cj1, cj2, cj36, cj45r, currentj1, currentj36):
    j1 = cj1 - currentj1
    j2 = cj2
    j36 = cj36 - currentj36
    j45 = cj45r

    joint1_chs   = '@STEP 221,' + str(j1) + ',0,0,0,0,0,0'
    joint2_chs   = '@STEP 221,0,' + str(j2) + ',0,0,0,0,0'
    joint2_chsi  = '@STEP 221,0,' + str(-j2) + ',0,0,0,0,0'
    joint36_chs  = '@STEP 221,0,0,' + str(j36) + ',0,0,' + str(j36) + ',0'
    joint45_chs  = '@STEP 221,0,0,0,' + str(j45) + ',' + str(-j45) + ',0,0'
    joint45_chsi = '@STEP 221,0,0,0,' + str(-j45) + ',' + str(j45) + ',0,0'
    gp_cl = '@STEP 221,0,0,0,0,0,-110,0'

    for k in range(7):
        if k == 0:
            print(joint1_chs)
        elif k == 1:
            print(joint36_chs)
        elif k == 2:
            print(joint45_chs)
        elif k == 3:
            print(joint2_chs)
        elif k == 4:
            print(gp_cl)
        elif k == 5:
            print(joint2_chsi)
        else:
            print(joint45_chsi)

        if k == 0:
            if abs(j1) < 1000:
                pause(5.5)
            else:
                u1 = 0.5*(np.round((abs(j1)-1000),-1)/100) + 5.5
                pause(u1)
        elif k == 1:
            if abs(j36) <= 200:
                pause(2)
            else:
                u2 = 0.5*(np.round((abs(j36)-200),-1)/100) + 2
                pause(u2)
        elif k == 2:
            if abs(j45) <= 150:
                pause(1.5);
            else:
                u4 = 0.3*(np.round((abs(j45)-150),-1)/50) + 1.5
                pause(u4)
        elif k == 3:
            if j2 <= 250:
                pause(2.5)
            else:
                u4 = 1*(np.round((j2-250),-1)/250) + 2.5
                pause(u4)
        elif k == 5:
            if j2 <= 250:
                pause(2.5)
            else:
                u6 = 1*(np.round((j2-250),-1)/250) + 2.5
                pause(u6)
        elif k == 6:
            if abs(j45) <= 150:
                pause(1.5)
            else:
                u4 = 0.3*(np.round((abs(j45)-150),-1)/50) + 1.5
                pause(u4)
        else:
            pause(1.5)

    currentj1 = cj1
    currentj36 = cj36
    return currentj1, currentj36

def robot_turn2_2 (currentj1, currentj36):
    recoj1i  = '@STEP 221,-1050,0,0,0,0,0,0'
    recoj2   = '@STEP 221,0,700,0,0,0,0,0'
    recoj2i  = '@STEP 221,0,-700,0,0,0,0,0'
    turnj22  = '@STEP 221,0,520,0,0,0,0,0'
    turnj22i = '@STEP 221,0,-520,0,0,0,0,0'
    turnj366 = '@STEP 221,0,0,-390,0,0,-390,0'
    turnj45i = '@STEP 221,0,0,0,340,340,0,0'
    rotaj45i = '@STEP 221,0,0,0,770,-770,0,0'
    gp_op    = '@STEP 221,0,0,0,0,0,110,0'
    gp_cl    = '@STEP 221,0,0,0,0,0,-110,0'

    print(recoj1i)
    pause(6)
    print(recoj2)
    pause(4.5)
    print(gp_op)
    pause(1.5)
    print(recoj2i)
    pause(4.5)
    print(rotaj45i)
    pause(4.5)
    print(turnj45i)
    pause(2.5)
    print(turnj366)
    pause(3)
    print(turnj22)
    pause(3.5)
    print(gp_cl)
    pause(1.5)
    print(turnj22i)
    pause(3.5)

    currentj1 = 900
    currentj36 = -410
    return currentj1, currentj36

def calcu_position(predicted,posX,posY):
    import chesslocation
    L   = np.shape(posX)[0]
    new = np.zeros((L, 3))
    j1  = np.zeros(L).T
    j2  = np.zeros(L).T
    j36 = np.zeros(L).T
    j45 = np.zeros(L).T
    j45_rotate = np.zeros(L).T
    nxy = np.zeros((L,2))
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
        nxy[i,:] = new[i,0:2].copy()
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
    prior = np.zeros((33,9), dtype = object)
    chess = np.array([j1, j2, j36, j45, j45_rotate]).T
    b = [7 , 9 , 5 , 3 , 1 , 2 , 4 , 8 , 6 , 23, 25,
         21, 19, 17, 18, 20, 24, 22, 11, 10, 27, 26,
         33, 16, 12, 15, 13, 14, 32, 28, 31, 29, 30];
    for p in range(0,33):
         prior[p,:] = chesslocation.matrix[(b[p] - 1),:]
    order = np.zeros((L,5))
    index = np.full((L,5), -1)

    for a in range(0,L):
        w = np.where(predicted[a] == prior[:,0])[0]
        k = w.size
        order[a,0:k] = w;
        index[a,0:k] = w;
    return chess, order, index, prior