import numpy as np
srcx = 757.0
srcy = 444.0
camposi_x  = 682.3
camposi_y  = 494.7
camposi_xh = 1508.0
camposi_yh = 1509.0
chess_h    = 32.05
x = np.around(srcx +((chess_h * (camposi_x - srcx)) / camposi_xh),1)
y = np.around(srcy +((chess_h * (camposi_y - srcy)) / camposi_yh),1)

src = np.array([x, y, 1]).T

thx = 180
rotx = np.array([[1, 0, 0],
				 [0, np.cos(np.deg2rad(thx)), -np.sin(np.deg2rad(thx))],
				 [0, np.sin(np.deg2rad(thx)), np.cos(np.deg2rad(thx))]])

thz = 180.3
rotz = np.array([[np.cos(np.deg2rad(thz)), -np.sin(np.deg2rad(thz)), 0],
				 [np.sin(np.deg2rad(thz)), np.cos(np.deg2rad(thz)), 0],
				 [0, 0, 1]])

scale = np.array([[1, 0, 0], [0 ,1 ,0], [0 ,0 ,1]])
tran  = np.array([[1, 0, -512], [0, 1, 216.1], [0, 0, 1]])

new = np.around((rotx @ rotz @ tran @ scale @ src),2).T.copy()
nxy = new[0:2].copy()
rx = nxy[0]
ry = nxy[1]
degree = np.rad2deg(np.arctan2(ry,rx))
j1 = np.around(degree * 19.64)

new1 = new.copy()
nxy1 = nxy.copy()
rx1 = nxy1[0]
ry1 = nxy1[1]
srctheta2 = 38
srctheta3 = -86.6
pxldis = 0.0312
d = np.around(pxldis * np.sqrt(rx1**2 + ry1**2),2)
d_src = d.copy()

j45_rotate = 0
if d > 34.5:
	d = 34.5
	d_dif = d_src - d
	j45_theta = np.rad2deg(np.asin(d_dif/9.2))
	j45 = np.around(-j45_theta * 4.27)
	j45_rotate = 0
else:
	j45 = 0;
	j45_rotate = np.around((degree - 90) * 4.27)

p = np.sqrt(8.54**2 + d**2)
theta_a = np.rad2deg(np.arctan(8.54 / d))
theta_b = np.rad2deg(np.arccos((17.78**2 + 17.78**2 - p**2) / (2 * 17.78 * 17.78)))
theta_c = (180 - theta_b) / 2
theta_3 = -(theta_a + theta_c)
theta_2 = 180 - theta_a - theta_b - theta_c

j36 = np.around(-(theta_3 - srctheta3) * 11.55)
j2  = np.around(-(theta_2 - srctheta2) * 19.64)
z = [j1, j2, j36, j45, j45_rotate]


print("camposi_x = " +str(camposi_x))
print("camposi_xh = " +str(camposi_xh))
print("camposi_y = " +str(camposi_y))
print("camposi_yh = " +str(camposi_yh))
print("chess_h = " +str(chess_h))
print("d = " +str(d))
print("d_src = " +str(d_src))
print("degree = " +str(degree))
print("j1 = " +str(j1))
print("j2 = " +str(j2))
print("j36 = " +str(j36))
print("j45 = " +str(j45))
print("j45_rotate = " +str(j45_rotate))
print("new = " +str(new))
print("new1 = " +str(new1))
print("nxy = " +str(nxy))
print("nxy1 = " +str(nxy1))
print("p = " +str(p))
print("pxldis = " +str(pxldis))
print("rotx = " +str(rotx))
print("rotz = " +str(rotz))
print("rx = " +str(rx))
print("rx1 = " +str(rx1))
print("ry = " +str(ry))
print("ry1 = " +str(ry1))
print("scale = " +str(scale))
print("src = " +str(src))
print("srctheta2 = " +str(srctheta2))
print("srctheta3 = " +str(srctheta3))
print("srcx = " +str(srcx))
print("srcy = " +str(srcy))
print("theta_2 = " +str(theta_2))
print("theta_3 = " +str(theta_3))
print("theta_a = " +str(theta_a))
print("theta_b = " +str(theta_b))
print("theta_c = " +str(theta_c))
print("thx = " +str(thx))
print("thz = " +str(thz))
print("tran = " +str(tran))
print("x = " +str(x))
print("y = " +str(y))
print("z = " +str(z))
