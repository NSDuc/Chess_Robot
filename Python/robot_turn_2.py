import serial

def robot_turn_2 (s, currentj1, currentj36):
	j1 = -(currentj1 - 900)
	j36 = -(currentj36 + 400)

	turnj1   = '@STEP 221,' + str(j1) + ',0,0,0,0,0,0'
	recoj1   = '@STEP 221,1050,0,0,0,0,0,0'
	turnj2   = '@STEP 221,0,510,0,0,0,0,0'
	turnj2i  = '@STEP 221,0,-510,0,0,0,0,0'
	recoj2   = '@STEP 221,0,700,0,0,0,0,0'
	recoj2i  = '@STEP 221,0,-700,0,0,0,0,0'
	oj36     = '@STEP 221,0,0,' + str(j36) + ',0,0,' + str(j36) + ',0'
	turnj36i = '@STEP 221,0,0,380,0,0,380,0'
	turnj45  = '@STEP 221,0,0,0,-340,-340,0,0'
	rotaj45  = '@STEP 221,0,0,0,-770,770,0,0'
	gp_op    = '@STEP 221,0,0,0,0,0,110,0'
	gp_cl    = '@STEP 221,0,0,0,0,0,-110,0'

	for k in range(16):
	    if k == 0:
	        s.write(turnj1)
	    elif k == 1:
	        s.write(oj36)
	    elif k == 2:
	        s.write(turnj2)
	        pause(3.5)
	    elif k == 3:
	        s.write(gp_op)
	        pause(1.5)
	    elif k == 4:
	        s.write(turnj2i)
	        pause(3.5)
	    elif k == 5:
	        s.write(turnj36i)
	        pause(3);
	    elif k == 6:
	        s.write(turnj45)
	        pause(2.5)
	    elif k == 7:
	        s.write(recoj2)
	        pause(4.5)
	    elif k == 8:
	        s.write(gp_cl)
	        pause(1.5)
	    elif k == 9:
	        s.write(recoj2i)
	        pause(4.5)
	    elif k == 10:
	        s.write(rotaj45)
	        pause(4.5)
	    elif k == 11:
	        s.write(recoj2)
	        pause(4.5)
	    elif k == 12:
	        s.write(gp_op)
	        pause(1.5)
	    elif k == 13:
	        s.write(gp_cl)
	        pause(1.5)
	    elif k == 14:
	        s.write(recoj2i)
	        pause(4.5)
	    else:
	        s.write(recoj1)
	        pause(6)

	    if k == 1:
	        if abs(j1) < 1000:
	            pause(5.5);
	        else:
	            u1 = 0.5*(round((abs(j1)-1000),-1)/100) + 5.5;
	            pause(u1);
	    elif k == 2:
	        if abs(j36) <= 200
	            pause(2);
	        else:
	            u2 = 0.5*(round((abs(j36)-200),-1)/100) + 2;
	            pause(u2);
	currentj1 = 1050
	currentj36 = -20
	return currentj1, currentj36