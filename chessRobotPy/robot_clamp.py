# Generated with SMOP  0.41
from libsmop import *
# .\robot_clamp.m

    
@function
def robot_clamp(s=None,cj1=None,cj2=None,cj36=None,cj45r=None,currentj1=None,currentj36=None,*args,**kwargs):
    varargin = robot_clamp.varargin
    nargin = robot_clamp.nargin

    j1=cj1 - currentj1
# .\robot_clamp.m:2
    j2=copy(cj2)
# .\robot_clamp.m:3
    j36=cj36 - currentj36
# .\robot_clamp.m:4
    j45=copy(cj45r)
# .\robot_clamp.m:5
    #---------------------------robot action-------------------------------------
    joint1_chs=concat(['@STEP 221,',num2str(j1),',0,0,0,0,0,0'])
# .\robot_clamp.m:7
    joint2_chs=concat(['@STEP 221,0,',num2str(j2),',0,0,0,0,0'])
# .\robot_clamp.m:8
    joint2_chsi=concat(['@STEP 221,0,',num2str(- j2),',0,0,0,0,0'])
# .\robot_clamp.m:9
    joint36_chs=concat(['@STEP 221,0,0,',num2str(j36),',0,0,',num2str(j36),',0'])
# .\robot_clamp.m:10
    joint45_chs=concat(['@STEP 221,0,0,0,',num2str(j45),',',num2str(- j45),',0,0'])
# .\robot_clamp.m:11
    joint45_chsi=concat(['@STEP 221,0,0,0,',num2str(- j45),',',num2str(j45),',0,0'])
# .\robot_clamp.m:12
    #joint36_chsi = ['@STEP 221,0,0,',num2str(-j36),',0,0,',num2str(-j36),',0'];
#gp_op = ['@STEP 221,0,0,0,0,0,110,0'];
    gp_cl=concat(['@STEP 221,0,0,0,0,0,-110,0'])
# .\robot_clamp.m:15
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
            if j1 > 2000:
                u=dot(0.5,(round((j1 - 2000),- 1) / 100))
# .\robot_clamp.m:36
                pause(u)
            else:
                pause(0.3)
        clear('q')
        q=fread(s)
# .\robot_clamp.m:43
        if q(arange(end() - 1,end())) == concat([[49],[13]]):
            continue
        else:
            break
    
    currentj1=copy(cj1)
# .\robot_clamp.m:53
    currentj36=copy(cj36)
# .\robot_clamp.m:54
    return currentj1,currentj36
    
if __name__ == '__main__':
    pass
    
    #}