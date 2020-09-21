# Generated with SMOP  0.41
from libsmop import *
# .\robot_turn_2.m

    
@function
def robot_turn_2(s=None,currentj1=None,currentj36=None,*args,**kwargs):
    varargin = robot_turn_2.varargin
    nargin = robot_turn_2.nargin

    j1=- (currentj1 - 900)
# .\robot_turn_2.m:2
    j36=- (currentj36 + 400)
# .\robot_turn_2.m:3
    #---------------------------robot action-------------------------------------
    turnj1=concat(['@STEP 221,',num2str(j1),',0,0,0,0,0,0'])
# .\robot_turn_2.m:5
    recoj1=concat(['@STEP 221,1050,0,0,0,0,0,0'])
# .\robot_turn_2.m:6
    turnj2=concat(['@STEP 221,0,510,0,0,0,0,0'])
# .\robot_turn_2.m:8
    turnj2i=concat(['@STEP 221,0,-510,0,0,0,0,0'])
# .\robot_turn_2.m:9
    recoj2=concat(['@STEP 221,0,700,0,0,0,0,0'])
# .\robot_turn_2.m:10
    recoj2i=concat(['@STEP 221,0,-700,0,0,0,0,0'])
# .\robot_turn_2.m:11
    oj36=concat(['@STEP 221,0,0,',num2str(j36),',0,0,',num2str(j36),',0'])
# .\robot_turn_2.m:13
    turnj36i=concat(['@STEP 221,0,0,380,0,0,380,0'])
# .\robot_turn_2.m:14
    turnj45=concat(['@STEP 221,0,0,0,-340,-340,0,0'])
# .\robot_turn_2.m:16
    rotaj45=concat(['@STEP 221,0,0,0,-770,770,0,0'])
# .\robot_turn_2.m:17
    gp_op=concat(['@STEP 221,0,0,0,0,0,110,0'])
# .\robot_turn_2.m:19
    gp_cl=concat(['@STEP 221,0,0,0,0,0,-110,0'])
# .\robot_turn_2.m:20
    #---------------------------robot run-------------------------------------
    
    for k in arange(1,16).reshape(-1):
        if k == 1:
            fprintf(s,turnj1)
        else:
            if k == 2:
                fprintf(s,oj36)
            else:
                if k == 3:
                    fprintf(s,turnj2)
                    pause(3.5)
                else:
                    if k == 4:
                        fprintf(s,gp_op)
                        pause(1.5)
                    else:
                        if k == 5:
                            fprintf(s,turnj2i)
                            pause(3.5)
                        else:
                            if k == 6:
                                fprintf(s,turnj36i)
                                pause(3)
                            else:
                                if k == 7:
                                    fprintf(s,turnj45)
                                    pause(2.5)
                                else:
                                    if k == 8:
                                        fprintf(s,recoj2)
                                        pause(4.5)
                                    else:
                                        if k == 9:
                                            fprintf(s,gp_cl)
                                            pause(1.5)
                                        else:
                                            if k == 10:
                                                fprintf(s,recoj2i)
                                                pause(4.5)
                                            else:
                                                if k == 11:
                                                    fprintf(s,rotaj45)
                                                    pause(4.5)
                                                else:
                                                    if k == 12:
                                                        fprintf(s,recoj2)
                                                        pause(4.5)
                                                    else:
                                                        if k == 13:
                                                            fprintf(s,gp_op)
                                                            pause(1.5)
                                                        else:
                                                            if k == 14:
                                                                fprintf(s,gp_cl)
                                                                pause(1.5)
                                                            else:
                                                                if k == 15:
                                                                    fprintf(s,recoj2i)
                                                                    pause(4.5)
                                                                else:
                                                                    fprintf(s,recoj1)
                                                                    pause(6)
        #------------------------------------
        if k == 1:
            if abs(j1) < 1000:
                pause(5.5)
            else:
                u1=dot(0.5,(round((abs(j1) - 1000),- 1) / 100)) + 5.5
# .\robot_turn_2.m:77
                pause(u1)
        else:
            if k == 2:
                if abs(j36) <= 200:
                    pause(2)
                else:
                    u2=dot(0.5,(round((abs(j36) - 200),- 1) / 100)) + 2
# .\robot_turn_2.m:84
                    pause(u2)
    
    currentj1=1050
# .\robot_turn_2.m:89
    currentj36=- 20
# .\robot_turn_2.m:90
    return currentj1,currentj36
    
if __name__ == '__main__':
    pass
    
    #}