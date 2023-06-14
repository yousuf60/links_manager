from threading import Thread 
from time import time


class LongPress:
    #to make sure to break the thread
    untouched = False
    press_timeout = .3
    press_long = 0


    def pressed_btn(self):
        print(self.untouched)
        self.pressed = time()
        pressed_thread = Thread(target = self.still_touched)
        pressed_thread.start()

    def still_touched(self):
        timeout = False
        while not self.untouched:
            self.press_long = time() - self.pressed
            if self.press_long >= self.press_timeout:
                self.remove_self()
                timeout = True
                break
                  
        self.untouched = False
        if timeout :
            self.delete_data()

    def on_release_limit(self):
        self.untouched = True
        if self.press_long < self.press_timeout:
            press_long = 0
            return True 
        else:
            press_long = 0
            return False 
