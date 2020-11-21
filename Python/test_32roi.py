import catchroi
import ConvoNN as nn

import numpy as np
import cv2

CHESS_MATRIX = np.array([
	["rCannon", "rChariot", "rElephant", "rGuard", "rGeneral", "rHorse", "rSoldier", \
	 "bCannon", "bChariot", "bElephant", "bGuard", "bGeneral", "bHorse", "bSoldier", 'Unknown']])

CHESS_COUNTER = np.array([
	[2,2,2,2,1,2,5,\
	 2,2,2,2,1,2,5,0]])

ERROR_CASE = np.zeros((1,15), dtype=np.int)
if 1:
	IMAGE_FOLDER = "F:\\Outsource\\AllSampleNight\\"

	picnames = np.array([
		'Picture 0.jpg', 'Picture 1.jpg', 'Picture 2.jpg', 'Picture 3.jpg', \
		'Picture 4.jpg', 'Picture 5.jpg', 'Picture 6.jpg', 'Picture 7.jpg', \
		# 'Picture 100.jpg', 'Picture 101.jpg', 'Picture 191.jpg'\
		# 'Picture 198.jpg'\
		# 'Picture1.jpg', 'Picture2.jpg', 'Picture3.jpg', 'Picture4.jpg', \
		# 'Picture5.jpg', 'Picture6.jpg', 'Picture7.jpg' \
	])
else:
	IMAGE_FOLDER = "F:\\Outsource\\AllSampleDay\\"
	picnames = np.array([
		'Picture 1.jpg', 'Picture 2.jpg', 'Picture 3.jpg', 'Picture 4.jpg', 'Picture 5.jpg', \
		'Picture 6.jpg', 'Picture 7.jpg', 'Picture 8.jpg', 'Picture 9.jpg'
	])

failed_case = 0;

print("START")
for name in picnames:
	path_name = IMAGE_FOLDER + name
	image = cv2.imread(path_name)

	cnt_mtx = np.zeros((1,15), dtype=np.int)

	_, chess_img_list, _, _ = catchroi.detect_roi(image)
	for chess_img in chess_img_list:
		label = nn.ConvoNN(chess_img)[0]
		if label != 'Unknown':
			label = label[2:]
		index = np.where(CHESS_MATRIX == label)
		cnt_mtx[index] += 1

	if (cnt_mtx != CHESS_COUNTER).any():
		ERROR_CASE += np.abs(cnt_mtx-CHESS_COUNTER)
		print("cnt_mtx =", cnt_mtx)
		print("TEST CASE ", name, " FAILED !")
		failed_case += 1
	else:
		print("TEST CASE ", name, " SUCCESS !")

print("failed_case = ", failed_case, "/", picnames.size)
for col in range(ERROR_CASE.size):
	err = ERROR_CASE[:,col]
	if err > 0:
		print(ERROR_CASE[:,col],"Error for CHESS", CHESS_MATRIX[:,col])
