from kivy.lang import Builder
from kivy.factory import Factory as F
from kivy.clock import mainthread

from time import time
from threading import Thread 
from threading import Event 

Builder.load_string("""
<Card>:
    size_hint_y: None
    height: "70dp"
    
    canvas.before:
        Color:
            rgba: 0, 0, 1, .4
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        id: lbl
        text: ""
        padding: "5dp"
""")


class Card(F.ButtonBehavior, F.BoxLayout):
    thr_event = Event()
    press_timeout = .3
    def __init__(self,link, color = (), text = "", *args, **kwargs):
        super().__init__(*args, **kwargs)
        if color:
            self.ids.lbl.color = color
        if text:
            self.ids.lbl.text = text
        self.link = link
        

    def on_press(self):
        
        self.pressed = time()
        pressed_thread = Thread(target = self.still_touched)
        pressed_thread.start()
    
    def still_touched(self):
        while not self.thr_event.is_set():
            self.press_long = time() - self.pressed
            if self.press_long >= self.press_timeout:
                self.remove_self()
                break
                  

        self.thr_event.clear()
        
    def on_release(self):
        self.thr_event.set()
        if self.press_long < self.press_timeout:
            print(self.link)

    @mainthread
    def remove_self(self):
        print(self.parent)
        self.parent.remove(self)