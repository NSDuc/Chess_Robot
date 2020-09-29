import numpy as np
    
def robot_clamp(s=None,cj1=None,cj2=None,cj36=None,cj45r=None,currentj1=None,currentj36=None,*args,**kwargs):
    j1 = cj1 - currentj1
    j2 = np.copy(cj2)
    j36 = cj36 - currentj36
    j45 = np.copy(cj45r)
    #---------------------------robot action-------------------------------------
    joint1_chs  = '@STEP 221,' + str(j1) + ',0,0,0,0,0,0'
    joint2_chs  = '@STEP 221,0,' + str(j2) + ',0,0,0,0,0'
    joint2_chsi = '@STEP 221,0,' + str(- j2) + ',0,0,0,0,0'
    joint36_chs = '@STEP 221,0,0,' + str(j36) + ',0,0,' + str(j36),',0'
    joint45_chs = '@STEP 221,0,0,0,' + str(j45) + ','  + str(- j45),',0,0'
    joint45_chsi= '@STEP 221,0,0,0,' + str(- j45) + ',' + str(j45),',0,0'

    gp_cl = '@STEP 221,0,0,0,0,0,-110,0'
# .\robot_clamp.m:15
    #---------------------------robot run-------------------------------------
    for k in range(1,8)
        if k == 1:
            fprintf(s,joint1_chs)
        elif k == 2:
            fprintf(s,joint36_chs)
        elif k == 3:
            fprintf(s,joint45_chs)
        elif k == 4:
            fprintf(s,joint2_chs)
        elif k == 5:
            fprintf(s,gp_cl)
        elif k == 6:
            fprintf(s,joint2_chsi)
        else:
            fprintf(s,joint45_chsi)
        #--------------------------
        if k == 1:
            if j1 > 2000:
                u=0.5 * np.round((j1 - 2000),- 1) / 100
                pause(u)
            else:
                pause(0.3)
        #clear('q')
        q = fread(s)
        if q[end-1:end] = [49;13]
            continue
        else:
            break

    currentj1 = np.copy(cj1)
    currentj36= np.copy(cj36)

    return currentj1,currentj36
    
