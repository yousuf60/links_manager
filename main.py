from kivy.app import App
from kivy.factory import Factory as F
from kivy.clock import mainthread


from libs import Box
from libs import RContainer

from threading import Thread
from threading import Event
import asyncio
from time import sleep
class Main(App):
    event = Event()
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
    def on_start(self):
        self.cont = RContainer()
        self.root.ids.rcycle.add_widget(self.cont)
        def a():
            lenth = 100
            print(len(list()))
            
            
            for i in range(100):
                #sleep(1)
                if self.event.is_set():
                    return
                
                self.add(i, self.cont)
        Thread(target=a).start()
        print(self.root.ids.bx.children)
    def on_stop(self):
        self.event.set()
    @mainthread
    def add(self, i, widget):
        widget.add(F.Button(text = str(i), size_hint = (1, None), height = "70dp"))


main=Main()
main.run()