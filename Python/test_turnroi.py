import catchroi
import ConvoNN as nn

import numpy as np
import cv2
CHESS_MATRIX = np.array([
	["rCannon", "rChariot", "rElephant", "rGeneral", "rGuard", "rHorse", "rSoldier", \
	 "bCannon", "bChariot", "bElephant", "bGeneral", "bGuard", "bHorse", "bSoldier"]])

CHESS_COUNTER = np.array([
	[2,2,2,1,2,2,5, \
	 2,2,2,1,2,2,5]])

ERROR_CASE = np.zeros((1,14), dtype=np.int)
if 1:
	IMAGE_FOLDER = "F:\\Outsource\\AllSampleNight\\"

	picnames = np.array(
		['Picture 8.jpg', 'Picture 9.jpg', 'Picture 10.jpg', 'Picture 11.jpg', \
		 'Picture 12.jpg', 'Picture 13.jpg', 'Picture 14.jpg', 'Picture 15.jpg', \
		 'Picture 16.jpg', 'Picture 17.jpg', 'Picture 18.jpg', 'Picture 19.jpg', \
		 'Picture 20.jpg', 'Picture 21.jpg'])
	results = np.array(
		['bCannon', 'bGuard', 'rCannon', 'bElephant', \
		 'rElephant', 'rHorse', 'rSoldier', 'bHorse', \
		 'rChariot', 'rGuard', 'bChariot', 'bSoldier', \
		 'bGeneral', 'rGeneral'])
# else:
	# IMAGE_FOLDER = "F:\\Outsource\\AllSampleDay\\"
	# picnames = np.array(['Picture 1.jpg', 'Picture 2.jpg', 'Picture 3.jpg', 'Picture 4.jpg', 'Picture 5.jpg', \
	# 					 'Picture 6.jpg', 'Picture 7.jpg', 'Picture 8.jpg', 'Picture 9.jpg'])

failed_case = 0;

print("START")
for i in range(picnames.size):
	name = picnames[i]
	res_ref = results[i]
	
	path_name = IMAGE_FOLDER + name
	image = cv2.imread(path_name)

	_, _, roi = catchroi.detect_turned_roi(image)
	# imshow('roi', roi)

	label, bw_chess = nn.ConvoNN(roi)
	label = label[2:]

	if (label != res_ref):
		failed_case += 1
		ind = np.where(CHESS_MATRIX == label)
		ERROR_CASE[ind] += 1
		print("TEST CASE ", name, " FAILED !")
	else:
		print("TEST CASE ", name, " SUCCESS !")
	print("Predict from/to:", res_ref, label)

print("failed_case = ", failed_case, "/", picnames.size)
for col in range(ERROR_CASE.size):
	err = ERROR_CASE[:,col]
	if err > 0:
		print(ERROR_CASE[:,col],"Error for CHESS", CHESS_MATRIX[:,col])
