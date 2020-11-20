import threading

def init():
  global import_picture
  global print_pause
  global print_serial
  global test_turncatch
  global is_stop
  global stop_cond
  global is_off

  import_picture = True
  print_pause    = True
  print_serial   = True
  test_turncatch = False

  is_stop = False
  stop_cond = threading.Condition()