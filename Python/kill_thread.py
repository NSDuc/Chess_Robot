# Python program raising 
# exceptions in a python 
# thread 
  
import threading 
import ctypes 
import time 

def print_name (name):
    while True:
        print('running ' + name)

class thread_with_exception(threading.Thread): 
    def __init__(self, name, func): 
        threading.Thread.__init__(self) 
        self.name = name
        self.func = func

    def run(self): 
        # target function of the thread class 
        try: 
            self.func()
        finally: 
            print('thread ended') 
           
    def get_id(self): 
  
        # returns id of the respective thread 
        if hasattr(self, '_thread_id'): 
            return self._thread_id 
        for id, thread in threading._active.items(): 
            if thread is self: 
                return id
   
    def raise_exception(self): 
        thread_id = self.get_id() 
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 
              ctypes.py_object(SystemExit)) 
        if res > 1: 
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0) 
            print('Exception raise failure') 

def test():
    t1 = thread_with_exception('Thread 1', print_name) 
    t1.start() 
    time.sleep(2) 
    t1.raise_exception() 
    t1.join()

# test()