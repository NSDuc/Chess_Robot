# Generated with SMOP  0.41
from libsmop import *
# .\robot_clamp2.m

    
@function
def robot_clamp2(s=None,cj1=None,cj2=None,cj36=None,cj45r=None,currentj1=None,currentj36=None,*args,**kwargs):
    varargin = robot_clamp2.varargin
    nargin = robot_clamp2.nargin

    j1=cj1 - currentj1
# .\robot_clamp2.m:2
    j2=copy(cj2)
# .\robot_clamp2.m:3
    j36=cj36 - currentj36
# .\robot_clamp2.m:4
    j45=copy(cj45r)
# .\robot_clamp2.m:5
    #---------------------------robot action-------------------------------------
    joint1_chs=concat(['@STEP 221,',num2str(j1),',0,0,0,0,0,0'])
# .\robot_clamp2.m:7
    joint2_chs=concat(['@STEP 221,0,',num2str(j2),',0,0,0,0,0'])
# .\robot_clamp2.m:8
    joint2_chsi=concat(['@STEP 221,0,',num2str(- j2),',0,0,0,0,0'])
# .\robot_clamp2.m:9
    joint36_chs=concat(['@STEP 221,0,0,',num2str(j36),',0,0,',num2str(j36),',0'])
# .\robot_clamp2.m:10
    joint45_chs=concat(['@STEP 221,0,0,0,',num2str(j45),',',num2str(- j45),',0,0'])
# .\robot_clamp2.m:11
    joint45_chsi=concat(['@STEP 221,0,0,0,',num2str(- j45),',',num2str(j45),',0,0'])
# .\robot_clamp2.m:12
    #joint36_chsi = ['@STEP 221,0,0,',num2str(-j36),',0,0,',num2str(-j36),',0'];
#gp_op = ['@STEP 221,0,0,0,0,0,110,0'];
    gp_cl=concat(['@STEP 221,0,0,0,0,0,-110,0'])
# .\robot_clamp2.m:15
    #---------------------------robot run-------------------------------------
    for k in arange(1,7).reshape(-1):
        if k == 1:
            fprintf(s,joint1_chs)
        else:
            if k == 2:
                fprintf(s,joint36_chs)
            else:
                if k == 3:
                    fprintf(s,joint45_chs)
                else:
                    if k == 4:
                        fprintf(s,joint2_chs)
                    else:
                        if k == 5:
                            fprintf(s,gp_cl)
                        else:
                            if k == 6:
                                fprintf(s,joint2_chsi)
                            else:
                                fprintf(s,joint45_chsi)
        #--------------------------
        if k == 1:
            if abs(j1) < 1000:
                pause(5.5)
            else:
                u1=dot(0.5,(round((abs(j1) - 1000),- 1) / 100)) + 5.5
# .\robot_clamp2.m:38
                pause(u1)
        else:
            if k == 2:
                if abs(j36) <= 200:
                    pause(2)
                else:
                    u2=dot(0.5,(round((abs(j36) - 200),- 1) / 100)) + 2
# .\robot_clamp2.m:45
                    pause(u2)
            else:
                if k == 3:
                    if abs(j45) <= 150:
                        pause(1.5)
                    else:
                        u4=dot(0.3,(round((abs(j45) - 150),- 1) / 50)) + 1.5
# .\robot_clamp2.m:52
                        pause(u4)
                else:
                    if k == 4:
                        if j2 <= 250:
                            pause(2.5)
                        else:
                            u4=dot(1,(round((j2 - 250),- 1) / 250)) + 2.5
# .\robot_clamp2.m:59
                            pause(u4)
                    else:
                        if k == 6:
                            if j2 <= 250:
                                pause(2.5)
                            else:
                                u6=dot(1,(round((j2 - 250),- 1) / 250)) + 2.5
# .\robot_clamp2.m:66
                                pause(u6)
                        else:
                            if k == 7:
                                if abs(j45) <= 150:
                                    pause(1.5)
                                else:
                                    u4=dot(0.3,(round((abs(j45) - 150),- 1) / 50)) + 1.5
# .\robot_clamp2.m:73
                                    pause(u4)
                            else:
                                pause(1.5)
    
    currentj1=copy(cj1)
# .\robot_clamp2.m:80
    currentj36=copy(cj36)
# .\robot_clamp2.m:81
    return currentj1,currentj36
    
if __name__ == '__main__':
    pass
    
    #}