# Generated with SMOP  0.41
from libsmop import *
# .\robot_place.m

    
@function
def robot_place(s=None,tj1=None,tj2=None,tj36=None,tj45p=None,tj45r=None,currentj1=None,currentj36=None,*args,**kwargs):
    varargin = robot_place.varargin
    nargin = robot_place.nargin

    j1=tj1 - currentj1
# .\robot_place.m:2
    j2=copy(tj2)
# .\robot_place.m:3
    j36=tj36 - currentj36
# .\robot_place.m:4
    j45p=copy(tj45p)
# .\robot_place.m:5
    j45r=copy(tj45r)
# .\robot_place.m:6
    #---------------------------robot action-------------------------------------
    joint1_tag=concat(['@STEP 221,',num2str(j1),',0,0,0,0,0,0'])
# .\robot_place.m:8
    joint2_tag=concat(['@STEP 221,0,',num2str(j2),',0,0,0,0,0'])
# .\robot_place.m:9
    joint2_tagsi=concat(['@STEP 221,0,',num2str(- j2),',0,0,0,0,0'])
# .\robot_place.m:10
    joint36_tag=concat(['@STEP 221,0,0,',num2str(j36),',0,0,',num2str(j36),',0'])
# .\robot_place.m:11
    #joint36_tagi = ['@STEP 221,0,0,',num2str(-j36),',0,0,',num2str(-j36),',0'];
    joint45p_tag=concat(['@STEP 221,0,0,0,',num2str(j45p),',',num2str(j45p),',0,0'])
# .\robot_place.m:13
    joint45p_tagi=concat(['@STEP 221,0,0,0,',num2str(- j45p),',',num2str(- j45p),',0,0'])
# .\robot_place.m:14
    joint45r_tag=concat(['@STEP 221,0,0,0,',num2str(j45r),',',num2str(- j45r),',0,0'])
# .\robot_place.m:15
    
    joint45r_tagi=concat(['@STEP 221,0,0,0,',num2str(- j45r),',',num2str(j45r),',0,0'])
# .\robot_place.m:16
    gp_op=concat(['@STEP 221,0,0,0,0,0,110,0'])
# .\robot_place.m:17
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
# .\robot_place.m:44
        clear('q')
        q=fread(s)
# .\robot_place.m:47
        if q(arange(end() - 1,end())) == concat([[49],[13]]):
            continue
        else:
            break
    
    currentj1=copy(tj1)
# .\robot_place.m:55
    currentj36=copy(tj36)
# .\robot_place.m:56
    return currentj1,currentj36,check
    
if __name__ == '__main__':
    pass
    
    #}