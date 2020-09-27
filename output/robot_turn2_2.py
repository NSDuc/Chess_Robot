import serial

def robot_turn2_2 (s, currentj1, currentj36):
	recoj1i  = '@STEP 221,-1050,0,0,0,0,0,0'
	recoj2   = '@STEP 221,0,700,0,0,0,0,0'
	recoj2i  = '@STEP 221,0,-700,0,0,0,0,0'
	turnj22  = '@STEP 221,0,520,0,0,0,0,0'
	turnj22i = '@STEP 221,0,-520,0,0,0,0,0'
	turnj366 = '@STEP 221,0,0,-390,0,0,-390,0'
	turnj45i = '@STEP 221,0,0,0,340,340,0,0'
	rotaj45i = '@STEP 221,0,0,0,770,-770,0,0'
	gp_op    = '@STEP 221,0,0,0,0,0,110,0'
	gp_cl    = '@STEP 221,0,0,0,0,0,-110,0'

    s.write(recoj1i)
    pause(6)
    s.write(recoj2)
    pause(4.5)
    s.write(gp_op)
    pause(1.5)
    s.write(recoj2i)
    pause(4.5)
    s.write(rotaj45i)
    pause(4.5)
    s.write(turnj45i)
    pause(2.5)
    s.write(turnj366)
    pause(3)
    s.write(turnj22)
    pause(3.5)
    s.write(gp_cl)
    pause(1.5)
    s.write(turnj22i)
    pause(3.5)

	currentj1 = 900
	currentj36 = -410

	return currentj1, currentj36