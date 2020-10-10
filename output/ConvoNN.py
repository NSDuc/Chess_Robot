import cv2
import numpy as np
import preprocess

chess_label = ['Cannon', 'Chariot', 'Elephant', 'General', 'Guard', 'Horse', 'Sodier']

def ConvoNN(raw_chess, model_red, model_black):
  global chess_label
  b,g,r = cv2.split(raw_chess)
  gb = g-b
  rb = r-b
  median_gb = gb.mean()
  median_rb = rb.mean()
  gray = cv2.cvtColor(raw_chess, cv2.COLOR_BGR2GRAY)
  gray = cv2.resize(gray, dsize=(90, 90), interpolation=cv2.INTER_LINEAR)

  if (median_rb > median_gb and median_rb >= 5):
    bw_chess = preprocess.process (gray, 0.66)
    X = np.reshape(bw_chess,[1,90,90,1])
    label_index = model_red.predict_classes(X)[0]
    label = 'r' + chess_label[label_index]
  elif (median_gb > median_rb and median_gb >= 15):
    label = 'Unknown'
    bw = cv2.threshold(gray, 0.38, 255, cv2.THRESH_BINARY)[1]
    bw_chess = 255 - bw
  else:
    bw_chess = preprocess.process (gray, 0.65)
    X = np.reshape(bw_chess,[1,90,90,1])
    label_index = model_black.predict_classes(X)[0]
    label = 'b' + chess_label[label_index]
  return label, bw_chess
