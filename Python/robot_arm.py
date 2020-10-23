import numpy as np
import time
import serial

import test_param

def init_sequence ():
    global seq
    seq = 0

def pause(t): #apply
    if test_param.print_pause:
        print("pause ", t)
    else:
        time.sleep(t)

def writeSerial(robot, matlab, data, p=2): #apply
    global seq
    if test_param.print_serial:
        print("writeSerial: " + data)
    else:
        robot.write((data + ", 0\r").encode("ascii"))
        matlab.write((data + ", " + str(p) + ', ' + str(seq) + ", 0\r").encode("ascii"))
        pause(2)
        seq += 1
        if (seq == 1000):
            seq = 0


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

def robot_place2(robot, matlab, tj1 ,tj2 ,tj36 ,tj45p ,tj45r ,currentj1 ,currentj36):
    print("\nrobot_place2 start")
    j1 = tj1 - currentj1
    j2 = tj2
    j36 = tj36 - currentj36
    j45p= tj45p
    j45r= tj45r
    #---------------------------robot action-------------------------------------
    joint1_tag= '@STEP 221, ' + str(j1) + ', 0, 0, 0, 0, 0'
    joint2_tag= '@STEP 221, 0, ' + str(j2) + ', 0, 0, 0, 0'
    joint2_tagsi= '@STEP 221, 0, ' + str(-j2) + ', 0, 0, 0, 0'
    joint36_tag= '@STEP 221, 0, 0, ' + str(j36) + ', 0, 0, ' + str(j36)
    joint45p_tag= '@STEP 221, 0, 0, 0, ' + str(j45p) + ', ' + str(j45p) + ', 0'
    joint45p_tagi= '@STEP 221, 0, 0, 0, ' + str(- j45p)+ ', ' + str(-j45p) + ', 0'
    joint45r_tag= '@STEP 221, 0, 0, 0, ' + str(j45r) + ', ' + str(-j45r) + ', 0'   
    joint45r_tagi= '@STEP 221, 0, 0, 0, ' + str(- j45r) + ', ' + str(j45r) + ', 0'
    gp_op= '@STEP 221, 0, 0, 0, 0, 0, 110'
    #---------------------------robot run-------------------------------------

    if abs(j1) < 1000:
        p = 5.5
    else:
        p = 0.5*(np.round((abs(j1)-1000),-1)/100) + 5.5
    writeSerial(robot, matlab, joint1_tag, p)

    if abs(j36) <= 200:
        p = 2
    else:
        p = 0.5*(np.round((abs(j36)-200),-1)/100) + 2
    writeSerial(robot, matlab, joint36_tag, p)

    if abs(j45r) <= 150:
        p = 1.5
    else:
        p = 0.3*(np.round((abs(j45r)-150),-1)/50) + 1.5
    if j45r != 0:
        writeSerial(robot, matlab, joint45r_tag, p)
    else:
        writeSerial(robot, matlab, joint45p_tag, p)

    if j2 <= 250:
        p = 2.5
    else:
        p = 1*(np.round((j2-250),-1)/250) + 2.5
    writeSerial(robot, matlab, joint2_tag, p)

    p = 1.5
    writeSerial(robot, matlab, gp_op, p)

    if j2 <= 250:
        p = 2.5
    else:
        p = 1*(np.round((j2-250),-1)/250) + 2.5
    writeSerial(robot, matlab, joint2_tagsi, p)

    if abs(j45r) <= 150:
        p = 1.5
    else:
        p = 0.3*(np.round((abs(j45r)-150),-1)/50) + 1.5
    if j45r != 0:
        writeSerial(robot, matlab, joint45r_tagi, p)
    else:
        writeSerial(robot, matlab, joint45p_tagi, p)

    check = '1'
    
    currentj1  = tj1
    currentj36 = tj36
    return currentj1,currentj36,check
    

def robot_clamp2 (robot, matlab, cj1, cj2, cj36, cj45r, currentj1, currentj36):
    # writeSerial(s,"\nrobot_clamp2 start")
    j1 = cj1 - currentj1
    j2 = cj2
    j36 = cj36 - currentj36
    j45 = cj45r

    joint1_chs   = '@STEP 221, ' + str(j1) + ', 0, 0, 0, 0, 0'
    joint2_chs   = '@STEP 221, 0, ' + str(j2) + ', 0, 0, 0, 0'
    joint2_chsi  = '@STEP 221, 0, ' + str(-j2) + ', 0, 0, 0, 0'
    joint36_chs  = '@STEP 221, 0, 0,' + str(j36) + ', 0, 0, ' + str(j36)
    joint45_chs  = '@STEP 221, 0, 0, 0, ' + str(j45) + ', ' + str(-j45) + ', 0'
    joint45_chsi = '@STEP 221, 0, 0, 0, ' + str(-j45) + ', ' + str(j45) + ', 0'
    gp_cl = '@STEP 221, 0, 0, 0, 0, 0, -110'

    if abs(j1) < 1000:
        p = 5.5
    else:
        p = 0.5*(np.round((abs(j1)-1000),-1)/100) + 5.5
    writeSerial(robot, matlab, joint1_chs, p)

    if abs(j36) <= 200:
        p = 2
    else:
        p = 0.5*(np.round((abs(j36)-200),-1)/100) + 2
    writeSerial(robot, matlab, joint36_chs, p)

    if abs(j45) <= 150:
        p = 1.5
    else:
        p = 0.3*(np.round((abs(j45)-150),-1)/50) + 1.5
    writeSerial(robot, matlab, joint45_chs, p)

    if j2 <= 250:
        p =2.5
    else:
        p = 1*(np.round((j2-250),-1)/250) + 2.5
    writeSerial(robot, matlab, joint2_chs, p)

    p = 1.5
    writeSerial(robot, matlab, gp_cl, p)

    if j2 <= 250:
        p = 2.5
    else:
        p = 1*(np.round((j2-250),-1)/250) + 2.5
    writeSerial(robot, matlab, joint2_chsi, p)

    if abs(j45) <= 150:
        p = 1.5
    else:
        p = 0.3*(np.round((abs(j45)-150),-1)/50) + 1.5
    writeSerial(robot, matlab, joint45_chsi, p)

    currentj1 = cj1
    currentj36 = cj36
    return currentj1, currentj36

def robot_turn2_2 (robot, matlab, currentj1, currentj36):
    recoj1i  = '@STEP 221, -1050, 0, 0, 0, 0, 0'
    recoj2   = '@STEP 221, 0, 700, 0, 0, 0, 0'
    recoj2i  = '@STEP 221, 0, -700, 0, 0, 0, 0'
    turnj22  = '@STEP 221, 0, 520, 0, 0, 0, 0'
    turnj22i = '@STEP 221, 0, -520, 0, 0, 0, 0'
    turnj366 = '@STEP 221, 0, 0, -390, 0, 0, -390'
    turnj45i = '@STEP 221, 0, 0, 0, 340, 340, 0'
    rotaj45i = '@STEP 221, 0, 0, 0, 770, -770, 0'
    gp_op    = '@STEP 221, 0, 0, 0, 0, 0, 110'
    gp_cl    = '@STEP 221, 0, 0, 0, 0, 0, -110'

    writeSerial(robot, matlab, recoj1i, 6)
    writeSerial(robot, matlab, recoj2, 4.5)
    writeSerial(robot, matlab, gp_op, 1.5)
    writeSerial(robot, matlab, recoj2i, 4.5)
    writeSerial(robot, matlab, rotaj45i, 4.5)
    writeSerial(robot, matlab, turnj45i, 2.5)
    writeSerial(robot, matlab, turnj366, 3)
    writeSerial(robot, matlab, turnj22, 3.5)
    writeSerial(robot, matlab, gp_cl, 1.5)
    writeSerial(robot, matlab, turnj22i, 3.5)

    currentj1 = 900
    currentj36 = -410
    return currentj1, currentj36
