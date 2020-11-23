import catchroi
import ConvoNN as nn

import numpy as np
import cv2

def imshow(name, image):
  cv2.imshow(name, image)
  if cv2.waitKey(0) == ord('q'):
    exit()
  cv2.destroyWindow(name)

CHESS_MATRIX = np.array([
	["rCannon", "rChariot", "rElephant", "rGeneral", "rGuard", "rHorse", "rSoldier", \
	 "bCannon", "bChariot", "bElephant", "bGeneral", "bGuard", "bHorse", "bSoldier"]])

ERROR_CASE = np.zeros((1,15), dtype=np.int)
if 0:
	IMAGE_FOLDER = "F:\\Outsource\\Test2\\"

	picnames = np.array([
		'Picture 0.jpg', 'Picture 1.jpg', 'Picture 2.jpg', 'Picture 3.jpg', \
		'Picture 4.jpg', 'Picture 5.jpg', 'Picture 6.jpg', 'Picture 7.jpg', \
		'Picture 8.jpg', 'Picture 9.jpg', 'Picture 10.jpg', 'Picture 11.jpg', \
		'Picture 12.jpg', 'Picture 13.jpg', 'Picture 14.jpg', 'Picture 15.jpg', \
		'Picture 16.jpg', 'Picture 17.jpg', 'Picture 18.jpg', 'Picture 19.jpg', \

		'Picture 20.jpg', 'Picture 21.jpg', 'Picture 22.jpg', 'Picture 23.jpg', \
		'Picture 24.jpg', 'Picture 25.jpg', 'Picture 26.jpg', 'Picture 27.jpg', \
		'Picture 33.jpg', 'Picture 34.jpg', 'Picture 35.jpg', 'Picture 36.jpg', \
		'Picture 37.jpg'
	])

	results = np.array([
		'bElephant', 'rSoldier', 'bChariot', 'bChariot', \
		'rCannon', 'rChariot', 'bSoldier', 'bHorse', \
		'bGeneral', 'bSoldier', 'bGuard', 'rGuard', \
		'rChariot', 'rSoldier', 'rSoldier', 'bCannon', \
		'bSoldier', 'rElephant', 'rGuard', 'rSoldier', \

		'rCannon', 'bGuard', 'rSoldier', 'bHorse', \
		'rGuard', 'rCannon', 'bGuard', 'bCannon', \
		'bHorse', 'rGuard', 'rCannon', 'bGuard', \
		'bCannon'
	])
elif 0:
	IMAGE_FOLDER = "F:\\Outsource\\AllSampleDay\\"

	picnames = np.array([
		'Picture 11.jpg', 'Picture 12.jpg', 'Picture 13.jpg', 'Picture 14.jpg',\
		'Picture 15.jpg', 'Picture 16.jpg', 'Picture 17.jpg', 'Picture 18.jpg',\
		'Picture 19.jpg', 'Picture 20.jpg', 'Picture 21.jpg', 'Picture 22.jpg',\
		'Picture 23.jpg', 'Picture 24.jpg', 'Picture 25.jpg', 'Picture 26.jpg',\
		'Picture 27.jpg', 'Picture 28.jpg', 'Picture 29.jpg', 'Picture 30.jpg',\
		'Picture 31.jpg', 'Picture 32.jpg', 'Picture 33.jpg', 'Picture 34.jpg',\
		'Picture 35.jpg', 'Picture 36.jpg', 'Picture 37.jpg', 'Picture 38.jpg',\
		'Picture 39.jpg', 'Picture 40.jpg', 'Picture 41.jpg', 'Picture 42.jpg'
	])

	results = np.array([
		'bCannon', 'bChariot', 'bElephant', 'bGeneral', \
		'bGuard', 'bGuard', 'bHorse', 'bSoldier', \
		'bSoldier', 'bSoldier', 'bSoldier', 'bSoldier', \
		'rCannon', 'rChariot', 'bElephant', 'rElephant',\
		'rElephant', 'rGeneral', 'rHorse', 'rSoldier',\
		'rSoldier', 'rSoldier', 'bCannon', 'bChariot', \
		'bHorse', 'rCannon', 'rChariot', 'rGuard', \
		'rGuard', 'rHorse', 'rSoldier', 'rSoldier'\
	])
else:
	IMAGE_FOLDER = "F:\\Outsource\\AllSampleNight\\"

	picnames = np.array([
		'Picture 8.jpg', 'Picture 9.jpg', 'Picture 10.jpg', 'Picture 11.jpg', \
		'Picture 12.jpg', 'Picture 13.jpg', 'Picture 14.jpg', 'Picture 15.jpg', \
		'Picture 16.jpg', 'Picture 17.jpg', 'Picture 18.jpg', 'Picture 19.jpg', \
		'Picture 20.jpg', 'Picture 21.jpg', 'Picture 22.jpg', 'Picture 24.jpg', \
	])

	results = np.array([
		'bCannon', 'bGuard', 'rCannon', 'bElephant', \
		'rElephant', 'rHorse', 'rSoldier', 'bHorse', \
		'rChariot', 'rGuard', 'bChariot', 'bSoldier', \
		'bGeneral', 'rGeneral', 'bGeneral', 'bChariot'
	])

failed_case = 0;

print("START")
for i in range(picnames.size):
	name = picnames[i]
	print(name)
	res_ref = results[i]
	
	path_name = IMAGE_FOLDER + name
	image = cv2.imread(path_name)

	_, _, roi = catchroi.detect_turned_roi(image)

	label, bw_chess = nn.ConvoNN(roi)

	if (label[2:] != res_ref):
		failed_case += 1
		ind = np.where(CHESS_MATRIX == label)
		ERROR_CASE[ind] += 1
		print("TEST CASE ", name, " FAILED ! Predict from/to:", res_ref, label)
		imshow('bw_chess', bw_chess)
		imshow('roi', roi)

print("failed_case = ", failed_case, "/", picnames.size)
for col in range(ERROR_CASE.size):
	err = ERROR_CASE[:,col]
	if err > 0:
		print(ERROR_CASE[:,col],"Error for CHESS", CHESS_MATRIX[:,col])

