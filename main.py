from kivy.app import App
from kivy.factory import Factory as F
from kivy.clock import mainthread

from libs import Box
from libs import RContainer
from libs import Card

from threading import Thread
from threading import Event
import asyncio
from time import sleep


class scrz(F.Screen):pass

class Main(App):
    event = Event()
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
        
    def on_start(self):
        self.cont = RContainer()
        self.main_scr=scrz()
        self.root.ids.scrz_manager.add_widget(self.main_scr)
        self.main_scr.add_widget(self.cont)

        def a():
            lenth = 100
            
            for i in range(lenth):
                #sleep(1)
                if self.event.is_set():
                    return
                sleep(.0001)
                self.add(i, self.cont)
        Thread(target=a).start()
        print(self.root.ids.bx.children)
    def on_stop(self):
        self.event.set()
    @mainthread
    def add(self, i, widget):
        widget.add(Card(text = str(i)))


main=Main()
main.run()