from skimage import measure
from skimage.io import imread, imshow
from skimage.filters import gaussian, threshold_otsu
import matplotlib.pyplot as plt
import numpy as np
import cv2
import ConvoNN


def detect_roi(original):
  chess_list = []
  posX_list  = []
  posY_list  = []
  b,g,r = cv2.split(original)
  recognition = (0.1*r + 0.1*g + 0.8*b).astype(np.uint8)
  # imshow('recognition',cv2.resize(recognition, (640,590)))
  thresh = threshold_otsu (recognition)
  level  = int(thresh*0.72)
  _ , bw = cv2.threshold (recognition, level, 255, cv2.THRESH_BINARY_INV)

  # imshow('bw',cv2.resize(bw, (640,590)))

  se = np.array([[0,0,1,0,0],
                 [0,1,1,1,0],
                 [1,1,1,1,1],
                 [0,1,1,1,0],
                 [0,0,1,0,0]], np.uint8)


  openbw = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, se)
  # imshow('openbw',cv2.resize(openbw, (640,590)))
  
  se = np.array([[0,1,0],
                 [1,1,1],
                 [0,1,0]], np.uint8)

  se = np.ones((2,2))
  se_range = se.shape[0]
  regionprops_bw = cv2.erode(openbw, se, iterations = 1)

  # imshow('openbw',cv2.resize(openbw, (640,590)))

  labels = measure.label(regionprops_bw)
  props  = measure.regionprops(labels)

  num_chess = 0
  for prop in props:
    minr, minc, maxr, maxc = prop.bbox
    minr, minc, maxr, maxc = minr-se_range, minc-se_range, \
                             maxr+se_range, maxc+se_range
    width  = maxr - minr
    length = maxc - minc
    mean = openbw[minr:maxr, minc:maxc].mean(axis=0).mean(axis=0)

    if ((width/length > 0.8) and (width/length) < 1.2) and \
    ((width>=70) and (width<=135)) and ((length>=70) and (length<=135)) \
    and (mean > 50):
      centerX = prop.centroid[1]
      centerY = prop.centroid[0]
      centerX, centerY = int(centerX), int(centerY)

      if (length - (centerX - minc)*2) > 5:
        length = (centerX - minc)*2 + 1
      if (width - (centerY - minr)*2) > 5:
        width = (centerY - minr)*2 + 1
      # subimg  = original[minr:maxr, minc:maxc].copy()
      subimg = original[minr:minr+width, minc:minc+length, :].copy()
      posX_list.append(centerX)
      posY_list.append(centerY)
      chess_list.append(subimg)

      num_chess += 1
      # imshow('subimg', subimg)
      # subimg2[centerY-minr-2:centerY-minr+2, centerX-minc-2: centerX-minc+2] = (255,0,0)
      # imshow('subimg2', subimg2)
    # elif (width > 30) and (length > 30):
    #   print(mean)
    #   imshow('subimg_2',original[minr:maxr, minc:maxc])

  print("number of chess:", num_chess)
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
  Xc, Yc = 620, 640
  DX1, DX2, DY1, DY2 = Xc-100, Xc+100, Yc-100, Yc+100

  cropframe  = frame[DX1:DX2, DY1:DY2, :].copy()
  gray   = cv2.cvtColor (cropframe, cv2.COLOR_BGR2GRAY)
  # recogn = cv2.Canny (gray, 20, 120)
  recogn = cv2.blur(gray, (2,2))
  # imshow("recogn", recogn)
  # circles = cv2.HoughCircles (recogn, cv2.HOUGH_GRADIENT, 1, 40,
  #                             param1=128,param2=50,minRadius=20,maxRadius=60)
  circles = cv2.HoughCircles(recogn, cv2.HOUGH_GRADIENT, 1.2, 90,
                             param1=50,param2=50,minRadius=43,maxRadius=53)

  circles = np.round (circles[0, :]).astype(np.int)
  for (x, y, r) in circles:
    # cv2.circle (cropframe2, (x,y), r, (0, 0, 100), 1)
    # imshow('cropframe2', cropframe2)
    roi = cropframe[y-r:y+r, x-r:x+r, :].copy()
    # imshow('roi', roi)

  return DY1+y, DX1+x, roi

def test():
  picnames = [
    r"F:\nntest\testimg\Picture 100.jpg",
    r"F:\nntest\testimg\Picture 101.jpg",
    r"F:\nntest\testimg\Picture 160.jpg"
    # r"F:\nntest\testimg\Picture 1001.jpg",
    # r"F:\nntest\testimg\Picture 1002.jpg",
    # r"F:\nntest\testimg\Picture 1003.jpg",
    # r"F:\nntest\testimg\Picture 1004.jpg",
    # r"F:\nntest\testimg\Picture 1005.jpg",
    # r"F:\nntest\testimg\Picture 1006.jpg",
    # r"F:\nntest\testimg\Picture 1007.jpg"
  ]
  for picname in picnames:
    img = cv2.imread(picname)
    openbw, chess_list, posX_sort, posY_sort = detect_roi(img)
    for raw_chess in chess_list:
      label, bw_chess = ConvoNN.ConvoNN(raw_chess)
      # imshow("bw_chess", bw_chess)
      print(label)

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
    r"F:\nntest\testimg\Picture TC_12.jpg"
    r"F:\Outsource\Bug\Err8.jpg",
    r"F:\Outsource\Bug\Err9.jpg"
  ]
  for picname in picnames:
    frame = cv2.imread (picname)
    _, _, roi = detect_turned_roi(frame)
    # imshow('roi', roi)

    label, bw_chess = ConvoNN.ConvoNN(roi)
    print(label)


def im2bw(image, level):
  bw = np.zeros(image.shape)
  for i in range(bw.shape[0]):
    for j in range(bw.shape[1]):
      if(image[i,j] >= level):
        bw[i,j] = 255
  return bw

def imshow(name, image):
  cv2.imshow(name, image)
  if cv2.waitKey(0) == ord('q'):
    exit()
  cv2.destroyWindow(name)

# test()
# test_detect_turned_roi()