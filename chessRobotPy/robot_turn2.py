# Generated with SMOP  0.41
from libsmop import *
# .\robot_turn2.m

    
@function
def robot_turn2(s=None,currentj1=None,currentj36=None,*args,**kwargs):
    varargin = robot_turn2.varargin
    nargin = robot_turn2.nargin

    #---------------------------robot action-------------------------------------
    recoj1i=concat(['@STEP 221,-1050,0,0,0,0,0,0'])
# .\robot_turn2.m:3
    recoj2=concat(['@STEP 221,0,700,0,0,0,0,0'])
# .\robot_turn2.m:5
    recoj2i=concat(['@STEP 221,0,-700,0,0,0,0,0'])
# .\robot_turn2.m:6
    turnj22=concat(['@STEP 221,0,520,0,0,0,0,0'])
# .\robot_turn2.m:7
    turnj22i=concat(['@STEP 221,0,-520,0,0,0,0,0'])
# .\robot_turn2.m:8
    turnj366=concat(['@STEP 221,0,0,-390,0,0,-390,0'])
# .\robot_turn2.m:10
    turnj45i=concat(['@STEP 221,0,0,0,340,340,0,0'])
# .\robot_turn2.m:12
    rotaj45i=concat(['@STEP 221,0,0,0,770,-770,0,0'])
# .\robot_turn2.m:13
    gp_op=concat(['@STEP 221,0,0,0,0,0,110,0'])
# .\robot_turn2.m:15
    gp_cl=concat(['@STEP 221,0,0,0,0,0,-110,0'])
# .\robot_turn2.m:16
    #---------------------------robot run-------------------------------------
    
    for k in arange(1,10).reshape(-1):
        if k == 1:
            fprintf(s,recoj1i)
        else:
            if k == 2:
                fprintf(s,recoj2)
            else:
                if k == 3:
                    fprintf(s,gp_op)
                else:
                    if k == 4:
                        fprintf(s,recoj2i)
                    else:
                        if k == 5:
                            fprintf(s,rotaj45i)
                        else:
                            if k == 6:
                                fprintf(s,turnj45i)
                            else:
                                if k == 7:
                                    fprintf(s,turnj366)
                                else:
                                    if k == 8:
                                        fprintf(s,turnj22)
                                    else:
                                        if k == 9:
                                            fprintf(s,gp_cl)
                                        else:
                                            fprintf(s,turnj22i)
        clear('q')
        q=fread(s)
# .\robot_turn2.m:43
        if q(arange(end() - 1,end())) == concat([[49],[13]]):
            continue
        else:
            break
    
    currentj1=900
# .\robot_turn2.m:51
    currentj36=- 410
# .\robot_turn2.m:52
    return currentj1,currentj36
    
if __name__ == '__main__':
    pass
    
    #}