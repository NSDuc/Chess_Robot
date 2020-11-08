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
    if rect[2] > 70 and rect[3] > 70 and rect[2] < 110 and rect[3] < 110:
      regionXb = rect[0]
      regionXe = rect[0] + rect[2]
      regionYb = rect[1]
      regionYe = rect[1] + rect[3]
      centerX  = int(rect[0] + rect[2] / 2)
      centerY  = int(rect[1] + rect[3] / 2)
      if (len(posX_list) > 0) and (centerX == posX_list[-1]) and (centerY == posY_list[-1]):
        continue
      posX_list.append(centerX)
      posY_list.append(centerY)
      sub_image = openbw[regionYb:regionYe,regionXb:regionXe]
      chess_list.append(src[regionYb:regionYe,regionXb:regionXe].copy())

  posX = np.array(posX_list).T
  posY = np.array(posY_list).T

  sort_index = posX.argsort()
  posX_sort = np.empty_like(sort_index)
  posY_sort = np.empty_like(sort_index)
  chess_list_sort = []

  posX_sort[:] = posX[sort_index]
  posY_sort[:] = posY[sort_index]
  for index in sort_index:
    chess_list_sort.append(chess_list[index])

  return openbw, chess_list_sort, posX_sort, posY_sort

def turn_catch(src):
  dy = 540
  dx = 490
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
    x,y,w,h = cv2.boundingRect(con)
    if w > 70 and h > 70:
      print(x,y)
      regionXb = dx + x
      regionXe = dx + x + w
      regionYb = dy + y
      regionYe = dy + y + h
      print("w,h=", w,h)
      posX = int(x + w / 2)
      posY = int(y + h / 2)
      break

  return posX+dy, posY+dx