import numpy as np
import time.sleep as pause
import serial
    
@function
def robot_place2(s ,tj1 ,tj2 ,tj36 ,tj45p ,tj45r ,currentj1 ,currentj36):
    j1 = tj1 - currentj1
    j2 = tj2
    j36 = tj36 - currentj36
    j45p= tj45p
    j45r= tj45r
    #---------------------------robot action-------------------------------------
    joint1_tag= '@STEP 221,' + str(j1) + ',0,0,0,0,0,0'
    joint2_tag= '@STEP 221,0,' + str(j2) +',0,0,0,0,0'
    joint2_tagsi= '@STEP 221,0,' + str(-j2) + ',0,0,0,0,0'
    joint36_tag= '@STEP 221,0,0,' + str(j36) + ',0,0,' + str(j36),',0'
    joint45p_tag= '@STEP 221,0,0,0,' + str(j45p),',' + str(j45p),',0,0'
    joint45p_tagi= '@STEP 221,0,0,0,' + str(- j45p),',' + str(-j45p),',0,0'
    joint45r_tag= '@STEP 221,0,0,0,' + str(j45r) + ',' + str(-j45r),',0,0'   
    joint45r_tagi= '@STEP 221,0,0,0,' + str(- j45r) + ',' + str(j45r),',0,0'
    gp_op= '@STEP 221,0,0,0,0,0,110,0'
    #---------------------------robot run-------------------------------------
    
    for k in range(7):
        if k == 1:
            s.write(s,joint1_tag)
        elif k == 2:
            s.write(s,joint36_tag)
        elif k == 3:
            if j45r != 0:
                s.write(s,joint45r_tag)
            else:
                s.write(s,joint45p_tag)
        elif k == 4:
            s.write(s,joint2_tag)
        elif k == 5:
            s.write(s,gp_op)
        elif k == 6:
            s.write(s,joint2_tagsi)
        else:
            if j45r != 0:
                s.write(s,joint45r_tagi)
            else:
                s.write(s,joint45p_tagi)
            check='1'

        if k == 1:
            if abs(j1) < 1000:
                pause(5.5)
            else:
                u1 = 0.5*(np.round((abs(j1)-1000),-1)/100) + 5.5
                pause(u1)
        elif k == 2:
            if abs(j36) <= 200:
                pause(2)
            else:
                2 = 0.5*(np.round((abs(j36)-200),-1)/100) + 2
                pause(u2)
        elif k == 3:
            if abs(j45r) <= 150:
                pause(1.5)
            else:
                u4 = 0.3*(np.round((abs(j45r)-150),-1)/50) + 1.5
                pause(u4)
        elif k == 4:
            if j2 <= 250:
                pause(2.5)
            else:
                u4 = 1*(np.round((j2-250),-1)/250) + 2.5
                pause(u4)
        elif k == 6:
            if j2 <= 250:
                pause(2.5)
            else:
                u6 = 1*(np.round((j2-250),-1)/250) + 2.5
                pause(u6)
        elif k == 7:
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
    
