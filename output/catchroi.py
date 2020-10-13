import numpy as np
from skimage.filters import threshold_otsu
import cv2

def catchroi(src):
  chess_list = []
  src_clone  = src.copy()
  b,g,r = cv2.split(src)
  recognition = (0.1*r + 0.1*g + 0.8*b).astype(np.uint8)
  thresh = threshold_otsu (recognition)
  _ , bw = cv2.threshold (recognition, thresh*0.72, 255, cv2.THRESH_BINARY)

  bw = 255 - bw
  se = np.array([[0,0,1,0,0],
                 [0,1,1,1,0],
                 [1,1,1,1,1],
                 [0,1,1,1,0],
                 [0,0,1,0,0]], np.uint8)
  
  openbw = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, se)
  
  contours, hierarchy = cv2.findContours(openbw,  
    cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

  posX_list  = []
  posY_list  = []
  for con in contours:
    rect = cv2.boundingRect(con)
    if rect[2] > 70 and rect[3] > 70:
      regionXb = rect[0]
      regionXe = rect[0] + rect[2]
      regionYb = rect[1]
      regionYe = rect[1] + rect[3]
      posX_list.append(int(rect[0] + rect[2] / 2))
      posY_list.append(int(rect[1] + rect[3] / 2))
      sub_image = openbw[regionYb:regionYe,regionXb:regionXe]
      chess_list.append(src[regionYb:regionYe,regionXb:regionXe].copy())

  posX = np.array(posX_list).T
  posY = np.array(posY_list).T

  # Mark Position on image
  blue_dot = [255,0,0]
  for i in range(len(posX_list)):
    src_clone[(posY_list[i] - 2):(posY_list[i] + 2),(posX_list[i] - 2):(posX_list[i] + 2)] = blue_dot

  cv2.imwrite("dot.jpg",src_clone)

  return openbw, chess_list, posX, posY

def turn_catch(src):
  dy = 500
  dx = 530
  src_crop  = src[dy:(dy + 150),dx:(dx + 150)].copy()
  b,g,r = cv2.split(src_crop)
  recognition = (0.1*r + 0.1*g + 0.8*b).astype(np.uint8)
  thresh = threshold_otsu (recognition)
  _ , bw = cv2.threshold (recognition, thresh*0.72, 255, cv2.THRESH_BINARY)

  bw = 255 - bw
  se = np.array([[0,0,1,0,0],
                 [0,1,1,1,0],
                 [1,1,1,1,1],
                 [0,1,1,1,0],
                 [0,0,1,0,0]], np.uint8)

  openbw = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, se)

  contours, hierarchy = cv2.findContours(openbw,  
    cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

  for con in contours:
    rect = cv2.boundingRect(con)
    if rect[2] > 70 and rect[3] > 70:
      regionXb = dx + rect[0]
      regionXe = dx + rect[0] + rect[2]
      regionYb = dy + rect[1]
      regionYe = dy + rect[1] + rect[3]
      posX = int(rect[0] + rect[2] / 2)
      posY = int(rect[1] + rect[3] / 2)
      break

  return posX, posY