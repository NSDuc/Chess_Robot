import cv2
import numpy as np
import preprocess

chess_label = ['Cannon', 'Chariot', 'Elephant', 'General', 'Guard', 'Horse', 'Sodier']
chess_label2 = ['Chariot', 'Elephant', 'General']

def ConvoNN(raw_chess, model_red, model_red2, model_black):
  global chess_label
  global chess_label2
  b,g,r = cv2.split(raw_chess)
  gb = g-b
  rb = r-b
  gb = g.astype(np.int)-b.astype(np.int)
  rb = r.astype(np.int)-b.astype(np.int)
  gb[gb < 0] = 0
  gb = gb.astype(np.uint8)
  rb[rb < 0] = 0
  rb = rb.astype(np.uint8)
  median_gb = gb.mean()
  median_rb = rb.mean()
  gray = cv2.cvtColor(raw_chess, cv2.COLOR_BGR2GRAY)
  gray = cv2.resize(gray, dsize=(90, 90), interpolation=cv2.INTER_LINEAR)

  if (median_rb > median_gb and median_rb >= 5):
    bw_chess = preprocess.process (gray, 0.66)
    X = np.reshape(bw_chess,[1,90,90,1])
    label_index = model_red.predict_classes(X)[0]
    if (label_index == 1) or (label_index == 2) or (label_index == 3):
      label_index = model_red2.predict_classes(X)[0]
      label = 'r' + chess_label2[label_index]
    else:
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
