import numpy as np
def robot_clamp2 (s, cj1, cj2, cj36, cj45r, currentj1, currentj36):
	j1 = cj1 - currentj1
	j2 = cj2
	j36 = cj36 - currentj36
	j45 = cj45r

	joint1_chs   = '@STEP 221,' + str(j1) + ',0,0,0,0,0,0'
	joint2_chs   = '@STEP 221,0,' + str(j2) + ',0,0,0,0,0'
	joint2_chsi  = '@STEP 221,0,' + str(-j2) + ',0,0,0,0,0'
	joint36_chs  = '@STEP 221,0,0,' + str(j36) + ',0,0,' + str(j36) + ',0'
	joint45_chs  = '@STEP 221,0,0,0,' + str(j45) + ',' + str(-j45) + ',0,0'
	joint45_chsi = '@STEP 221,0,0,0,' + str(-j45) + ',' + str(j45) + ',0,0'
	gp_cl = '@STEP 221,0,0,0,0,0,-110,0'

	for k in range(7):
	    if k == 0:
	        s.write(joint1_chs)
	    elif k == 1:
	        s.write(joint36_chs)
	    elif k == 2:
	        s.write(joint45_chs)
	    elif k == 3:
	        s.write(joint2_chs)
	    elif k == 4:
	        s.write(gp_cl)
	    elif k == 5:
	        s.write(joint2_chsi)
	    else:
	        s.write(joint45_chsi)

	    if k == 1:
	        if abs(j1) < 1000:
	            pause(5.5)
	        else:
	            u1 = 0.5*(np.round((abs(j1)-1000),-1)/100) + 5.5
	            pause(u1)
	    elif k == 2:
	        if abs(j36) <= 200:
	            pause(2)
	        else:
	            u2 = 0.5*(np.round((abs(j36)-200),-1)/100) + 2
	            pause(u2)
	    elif k == 3:
	        if abs(j45) <= 150:
	            pause(1.5);
	        else:
	            u4 = 0.3*(np.round((abs(j45)-150),-1)/50) + 1.5
	            pause(u4)
	    elif k == 4:
	        if j2 <= 250:
	            pause(2.5)
	        else:
	            u4 = 1*(np.round((j2-250),-1)/250) + 2.5
	            pause(u4)
	    elif k == 6:
	        if j2 <= 250:
	            pause(2.5)
	        else:
	            u6 = 1*(np.round((j2-250),-1)/250) + 2.5
	            pause(u6)
	    elif k == 7:
	        if abs(j45) <= 150:
	            pause(1.5)
	        else:
	            u4 = 0.3*(np.round((abs(j45)-150),-1)/50) + 1.5
	            pause(u4)
	    else:
	        pause(1.5)

	currentj1 = cj1
	currentj36 = cj36
	return currentj1, currentj36