# Generated with SMOP  0.41
from libsmop import *
# .\robot_turn.m

    
@function
def robot_turn(s=None,currentj1=None,currentj36=None,*args,**kwargs):
    varargin = robot_turn.varargin
    nargin = robot_turn.nargin

    j1=- (currentj1 - 900)
# .\robot_turn.m:2
    j36=- (currentj36 + 400)
# .\robot_turn.m:3
    #---------------------------robot action-------------------------------------
    turnj1=concat(['@STEP 221,',num2str(j1),',0,0,0,0,0,0'])
# .\robot_turn.m:5
    recoj1=concat(['@STEP 221,1050,0,0,0,0,0,0'])
# .\robot_turn.m:6
    turnj2=concat(['@STEP 221,0,510,0,0,0,0,0'])
# .\robot_turn.m:8
    turnj2i=concat(['@STEP 221,0,-510,0,0,0,0,0'])
# .\robot_turn.m:9
    recoj2=concat(['@STEP 221,0,700,0,0,0,0,0'])
# .\robot_turn.m:10
    recoj2i=concat(['@STEP 221,0,-700,0,0,0,0,0'])
# .\robot_turn.m:11
    oj36=concat(['@STEP 221,0,0,',num2str(j36),',0,0,',num2str(j36),',0'])
# .\robot_turn.m:13
    turnj36i=concat(['@STEP 221,0,0,380,0,0,380,0'])
# .\robot_turn.m:14
    turnj45=concat(['@STEP 221,0,0,0,-340,-340,0,0'])
# .\robot_turn.m:16
    rotaj45=concat(['@STEP 221,0,0,0,-770,770,0,0'])
# .\robot_turn.m:17
    gp_op=concat(['@STEP 221,0,0,0,0,0,110,0'])
# .\robot_turn.m:19
    gp_cl=concat(['@STEP 221,0,0,0,0,0,-110,0'])
# .\robot_turn.m:20
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
                else:
                    if k == 4:
                        fprintf(s,gp_op)
                    else:
                        if k == 5:
                            fprintf(s,turnj2i)
                        else:
                            if k == 6:
                                fprintf(s,turnj36i)
                            else:
                                if k == 7:
                                    fprintf(s,turnj45)
                                else:
                                    if k == 8:
                                        fprintf(s,recoj2)
                                    else:
                                        if k == 9:
                                            fprintf(s,gp_cl)
                                        else:
                                            if k == 10:
                                                fprintf(s,recoj2i)
                                            else:
                                                if k == 11:
                                                    fprintf(s,rotaj45)
                                                else:
                                                    if k == 12:
                                                        fprintf(s,recoj2)
                                                    else:
                                                        if k == 13:
                                                            fprintf(s,gp_op)
                                                        else:
                                                            if k == 14:
                                                                fprintf(s,gp_cl)
                                                            else:
                                                                if k == 15:
                                                                    fprintf(s,recoj2i)
                                                                else:
                                                                    fprintf(s,recoj1)
        clear('q')
        q=fread(s)
# .\robot_turn.m:59
        if q(arange(end() - 1,end())) == concat([[49],[13]]):
            continue
        else:
            break
    
    currentj1=1050
# .\robot_turn.m:67
    currentj36=- 20
# .\robot_turn.m:68
    return currentj1,currentj36
    
if __name__ == '__main__':
    pass
    
    #}