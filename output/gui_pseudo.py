currentj1  = 0
currentj36 = 0
currentj6  = 0

def gui_init:
  return None


def gui_open_cb:
  currentj1  = 0
  currentj36 = 0
  currentj6  = 0


# Recognition
def callback_pushbutton1:
  # 1. Capture image to variable frame1 and show to variable axes1
  # 2. Run catchroi(frame): 
  #    openbw : black white image to axes3
  #    undistort image
  #    posX, posY: position of all roi on the table
  #    regionXb = c(selc,1);
  #    regionXe = c(selc,1) + c(selc,3);
  #    regionYb = c(selc,2);
  #    regionYe = c(selc,2) + c(selc,4);
  #    #roi1=src(regionYb(1):regionYe(1),regionXb(1):regionXe(1))
  #    #assignin('base','roi1',roi1);
  #    #roi = im2uint8(roi1);
  #    #roi = im2uint8(roi2);
  #    #roi = im2uint8(roi3);
  #    #roi = im2uint8(roi4);
  #  3. Show roi4 to axe5

  return None


# Start
def callback_pushbutton6:
  return None


# Connect
def callback_pushbutton2:
  return None

# Robot on/off
def callback_pushbutton7:
  return None

# Stop/Continue
def callback_pushbutton4:
  return None

# Exit
def callback_pushbutton5:
  return None


# uitable1 : predicted character | posX | posY