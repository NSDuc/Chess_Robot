from skimage import measure
from skimage.io import imread, imshow
from skimage.filters import gaussian, threshold_otsu
import matplotlib.pyplot as plt
import numpy as np
import cv2
import ConvoNN

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

def detect_roi(original):
  chess_list = []
  posX_list  = []
  posY_list  = []
  b,g,r = cv2.split(original)
  recognition = (0.1*r + 0.1*g + 0.8*b).astype(np.uint8)
  blurred = gaussian(recognition, sigma=.8)
  thresh = threshold_otsu (recognition)
  _ , bw = cv2.threshold (recognition, thresh*0.72, 255, cv2.THRESH_BINARY_INV)

  #bw = 255 - bw
  # cv2.imshow('bw',cv2.resize(bw, (640,590)))
  # cv2.waitKey(0)
  # cv2.destroyAllWindows()
  se = np.array([[0,0,1,0,0],
                 [0,1,1,1,0],
                 [1,1,1,1,1],
                 [0,1,1,1,0],
                 [0,0,1,0,0]], np.uint8)
  openbw = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, se)

  labels = measure.label(openbw)
  props  = measure.regionprops(labels)

  for prop in props:
    minr, minc, maxr, maxc = prop.bbox
    width  = maxr - minr
    length = maxc - minc
    diff_wl = np.abs(width-length)

    if (diff_wl <= 25) and (width>=75) and (width<=120) and (length>=75) and (length<=120):
      # centerX = (minr + maxr)/2
      # centerY = (minc + maxc)/2
      centerX = prop.centroid[1]
      centerY = prop.centroid[0]
      subimg = original[minr:maxr, minc:maxc].copy()
      posX_list.append(centerX)
      posY_list.append(centerY)
      chess_list.append(subimg)
      # cv2.imshow('subimg', subimg)
      # cv2.waitKey(0)
      # cv2.destroyAllWindows()

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



def detect_turned_roi(frame):
  Xc, Yc = 590, 640
  DX1, DX2, DY1, DY2 = Xc-100, Xc+100, Yc-100, Yc+100

  cropframe  = frame[DX1:DX2, DY1:DY2, :].copy()
  cropframe2 = cropframe.copy()
  # b, g, r = cv2.split(cropframe)
  # recogn  = (0.1*r + 0.1*g + 0.8*b).astype(np.uint8)

  gray   = cv2.cvtColor (cropframe, cv2.COLOR_BGR2GRAY)
  recogn = cv2.Canny (gray, 20, 120)
  # imshow("recogn", recogn)
  circles = cv2.HoughCircles (recogn, cv2.HOUGH_GRADIENT, 1, 40,
                              param1=128,param2=50,minRadius=20,maxRadius=60)
  # circles = cv2.HoughCircles(recogn, cv2.HOUGH_GRADIENT, 1, 100,
  #                            param1=100,param2=90,minRadius=30,maxRadius=70)


  circles = np.round (circles[0, :]).astype(np.int)
  for (x, y, r) in circles:
    # cv2.circle (cropframe2, (x,y), r, (0, 0, 100), 1)
    # imshow('cropframe2', cropframe2)
    roi = cropframe[y-r:y+r, x-r:x+r, :].copy()
    # imshow('roi', roi)

  return DY1+y, DX1+x, roi

def test():
  picname = r"F:\nntest\testimg\Picture 205.jpg"
  img = cv2.imread(picname)
  detect_roi(img)

  # picname = r"F:\nntest\testimg\Picture 101.jpg"
  # img = cv2.imread(picname)
  # detect_roi(img)


def test_detect_turned_roi():
  picnames = [ 
    r"F:\nntest\testimg\Picture 180.jpg",
    r"F:\nntest\testimg\Picture 181.jpg",
    r"F:\nntest\testimg\Picture 182.jpg",
    r"F:\nntest\testimg\Picture 183.jpg",
    r"F:\nntest\testimg\Picture 184.jpg",
    r"F:\nntest\testimg\Picture TC_11.jpg",
    r"F:\nntest\testimg\Picture TC_12.jpg"]
  for picname in picnames:
    frame = cv2.imread (picname)
    roi = detect_turned_roi(frame)
    imshow('roi', roi)

    label, bw_chess = ConvoNN.ConvoNN(roi)
    print(label)



def imshow(name, image):
  cv2.imshow(name, image)
  cv2.waitKey(0)
  cv2.destroyWindow(name)

# test()
# test_detect_turned_roi()