import cv2
import numpy as np
import preprocess
import cnn.train as train

chess_label2 = ['Chariot', 'Elephant', 'General', 'Soldier']

model_red = train.load_cnn2("./cnn/redA.pth")
model_black = train.load_cnn2("./cnn/blackA.pth")

def ConvoNN(raw_chess):
  global chess_label2
  b,g,r = cv2.split(raw_chess)
  gb = g.astype(np.int)-b.astype(np.int)
  rb = r.astype(np.int)-b.astype(np.int)
  gb[gb < 0] = 0
  gb = gb.astype(np.uint8)
  rb[rb < 0] = 0
  rb = rb.astype(np.uint8)
  median_gb = gb.mean()
  median_rb = rb.mean()
  img  = cv2.resize(raw_chess, dsize=(90, 90), interpolation=cv2.INTER_LINEAR)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  if (median_rb > median_gb and median_rb >= 5):
    bw_chess = preprocess.process (gray, 0.66)
    label = train.predict(model_red, bw_chess, 'r')
  elif (median_gb > median_rb and median_gb >= 14):
    label = 'Unknown'
    bw = cv2.threshold(gray, 0.38, 255, cv2.THRESH_BINARY)[1]
    bw_chess = 255 - bw
  else:
    bw_chess = preprocess.process (gray, 0.65)
    label = train.predict(model_black, bw_chess, 'b')
  return label, bw_chess
