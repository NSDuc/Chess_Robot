import numpy as np
import time
import serial

import test_param

def pause(t): #apply
    if test_param.print_pause:
        print("pause ", t)
    else:
        time.sleep(t)

def writeSerial(s, data): #apply
    if test_param.print_serial:
        print(s.port + ": " + data)
    else:
        s.write((data+"\r\n").encode("ascii"))

def readSerial(s):
    eol = b'\r'
    line = ""
    while True:
        c = s.read()
        if c:
            if c == eol:
                break
            else:
                line += c.decode('ascii')
        else:
            break
    return line

def robot_place2(s, tj1 ,tj2 ,tj36 ,tj45p ,tj45r ,currentj1 ,currentj36):
    print("\nrobot_place2 start")
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
            writeSerial(s,joint1_tag)
        elif k == 1:
            writeSerial(s,joint36_tag)
        elif k == 2:
            if j45r != 0:
                writeSerial(s,joint45r_tag)
            else:
                writeSerial(s,joint45p_tag)
        elif k == 3:
            writeSerial(s,joint2_tag)
        elif k == 4:
            writeSerial(s,gp_op)
        elif k == 5:
            writeSerial(s,joint2_tagsi)
        else:
            if j45r != 0:
                writeSerial(s,joint45r_tagi)
            else:
                writeSerial(s,joint45p_tagi)
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
    

def robot_clamp2 (s, cj1, cj2, cj36, cj45r, currentj1, currentj36):
    writeSerial(s,"\nrobot_clamp2 start")
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
            writeSerial(s,joint1_chs)
        elif k == 1:
            writeSerial(s,joint36_chs)
        elif k == 2:
            writeSerial(s,joint45_chs)
        elif k == 3:
            writeSerial(s,joint2_chs)
        elif k == 4:
            writeSerial(s,gp_cl)
        elif k == 5:
            writeSerial(s,joint2_chsi)
        else:
            writeSerial(s,joint45_chsi)

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

def robot_turn2_2 (s, currentj1, currentj36):
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

    writeSerial(s,recoj1i)
    pause(6)
    writeSerial(s,recoj2)
    pause(4.5)
    writeSerial(s,gp_op)
    pause(1.5)
    writeSerial(s,recoj2i)
    pause(4.5)
    writeSerial(s,rotaj45i)
    pause(4.5)
    writeSerial(s,turnj45i)
    pause(2.5)
    writeSerial(s,turnj366)
    pause(3)
    writeSerial(s,turnj22)
    pause(3.5)
    writeSerial(s,gp_cl)
    pause(1.5)
    writeSerial(s,turnj22i)
    pause(3.5)

    currentj1 = 900
    currentj36 = -410
    return currentj1, currentj36
