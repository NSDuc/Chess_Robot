import threading

def init():
  global import_picture
  global print_pause
  global print_serial
  global is_stop
  global stop_cond

  import_picture = False
  print_pause    = False
  print_serial   = True

  is_stop = False
  stop_cond = threading.Condition()