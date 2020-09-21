import cv2

load(fullfile('black2.mat'));
roi = im2uint8(roi1);

Q = ConvoNN(roi);

Q = blackpreprocess(Q);
cv2.imshow(Q);