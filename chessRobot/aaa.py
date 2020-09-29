import cv2

load(fullfile('black2.mat'))
roi = roi1.astype(np.uint8)

Q = ConvoNN(roi)

Q = blackpreprocess(Q)
cv2.imshow(Q)