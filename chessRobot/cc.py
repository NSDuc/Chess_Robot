#convert competed by nsduc97
#tested : 100% OK
import numpy as np

j1 = 1618
j2 = 140
j36 = -45
j45 = -0

theta_1 = j1 / 19.64
theta_2 = -j2 / 19.64 + 42.7
theta_3 = -j36 / 11.55 - 85
theta_4 = -j45 / 4.27 - 90
d = np.around(17.78*np.cos(np.deg2rad(theta_2)) + 17.78*np.cos(np.deg2rad(theta_3)) + 9.2*np.cos(np.deg2rad(theta_4)),2);
h = 17.78*np.sin(np.deg2rad(theta_2)) + 17.78*np.sin(np.deg2rad(theta_3)) + 9.2*np.sin(np.deg2rad(theta_4));
pixd = d / 0.0312;
rx = pixd*np.cos(np.deg2rad(theta_1));
ry = pixd*np.sin(np.deg2rad(theta_1));
