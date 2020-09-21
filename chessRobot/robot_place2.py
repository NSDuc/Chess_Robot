# Generated with SMOP  0.41
from libsmop import *
# .\robot_place2.m

    
@function
def robot_place2(s=None,tj1=None,tj2=None,tj36=None,tj45p=None,tj45r=None,currentj1=None,currentj36=None,*args,**kwargs):
    varargin = robot_place2.varargin
    nargin = robot_place2.nargin

    j1=tj1 - currentj1
# .\robot_place2.m:2
    j2=copy(tj2)
# .\robot_place2.m:3
    j36=tj36 - currentj36
# .\robot_place2.m:4
    j45p=copy(tj45p)
# .\robot_place2.m:5
    j45r=copy(tj45r)
# .\robot_place2.m:6
    #---------------------------robot action-------------------------------------
    joint1_tag=concat(['@STEP 221,',num2str(j1),',0,0,0,0,0,0'])
# .\robot_place2.m:8
    joint2_tag=concat(['@STEP 221,0,',num2str(j2),',0,0,0,0,0'])
# .\robot_place2.m:9
    joint2_tagsi=concat(['@STEP 221,0,',num2str(- j2),',0,0,0,0,0'])
# .\robot_place2.m:10
    joint36_tag=concat(['@STEP 221,0,0,',num2str(j36),',0,0,',num2str(j36),',0'])
# .\robot_place2.m:11
    #joint36_tagi = ['@STEP 221,0,0,',num2str(-j36),',0,0,',num2str(-j36),',0'];
    joint45p_tag=concat(['@STEP 221,0,0,0,',num2str(j45p),',',num2str(j45p),',0,0'])
# .\robot_place2.m:13
    joint45p_tagi=concat(['@STEP 221,0,0,0,',num2str(- j45p),',',num2str(- j45p),',0,0'])
# .\robot_place2.m:14
    joint45r_tag=concat(['@STEP 221,0,0,0,',num2str(j45r),',',num2str(- j45r),',0,0'])
# .\robot_place2.m:15
    
    joint45r_tagi=concat(['@STEP 221,0,0,0,',num2str(- j45r),',',num2str(j45r),',0,0'])
# .\robot_place2.m:16
    gp_op=concat(['@STEP 221,0,0,0,0,0,110,0'])
# .\robot_place2.m:17
    #gp_cl = ['@STEP 221,0,0,0,0,0,-110,0'];
#---------------------------robot run-------------------------------------
    
    for k in arange(1,7).reshape(-1):
        if k == 1:
            fprintf(s,joint1_tag)
        else:
            if k == 2:
                fprintf(s,joint36_tag)
            else:
                if k == 3:
                    if j45r != 0:
                        fprintf(s,joint45r_tag)
                    else:
                        fprintf(s,joint45p_tag)
                else:
                    if k == 4:
                        fprintf(s,joint2_tag)
                    else:
                        if k == 5:
                            fprintf(s,gp_op)
                        else:
                            if k == 6:
                                fprintf(s,joint2_tagsi)
                            else:
                                if j45r != 0:
                                    fprintf(s,joint45r_tagi)
                                else:
                                    fprintf(s,joint45p_tagi)
                                check='1'
# .\robot_place2.m:44
        #-------------------------
        if k == 1:
            if abs(j1) < 1000:
                pause(5.5)
            else:
                u1=dot(0.5,(round((abs(j1) - 1000),- 1) / 100)) + 5.5
# .\robot_place2.m:51
                pause(u1)
        else:
            if k == 2:
                if abs(j36) <= 200:
                    pause(2)
                else:
                    u2=dot(0.5,(round((abs(j36) - 200),- 1) / 100)) + 2
# .\robot_place2.m:58
                    pause(u2)
            else:
                if k == 3:
                    if abs(j45r) <= 150:
                        pause(1.5)
                    else:
                        u4=dot(0.3,(round((abs(j45r) - 150),- 1) / 50)) + 1.5
# .\robot_place2.m:65
                        pause(u4)
                else:
                    if k == 4:
                        if j2 <= 250:
                            pause(2.5)
                        else:
                            u4=dot(1,(round((j2 - 250),- 1) / 250)) + 2.5
# .\robot_place2.m:72
                            pause(u4)
                    else:
                        if k == 6:
                            if j2 <= 250:
                                pause(2.5)
                            else:
                                u6=dot(1,(round((j2 - 250),- 1) / 250)) + 2.5
# .\robot_place2.m:79
                                pause(u6)
                        else:
                            if k == 7:
                                if abs(j45r) <= 150:
                                    pause(1.5)
                                else:
                                    u4=dot(0.3,(round((abs(j45r) - 150),- 1) / 50)) + 1.5
# .\robot_place2.m:86
                                    pause(u4)
                            else:
                                pause(1.5)
    
    currentj1=copy(tj1)
# .\robot_place2.m:93
    currentj36=copy(tj36)
# .\robot_place2.m:94
    return currentj1,currentj36,check
    
if __name__ == '__main__':
    pass
    
    #}