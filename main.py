from kivy.app import App
from kivy.factory import Factory as F
from kivy.clock import mainthread

from libs import Box
from libs import RContainer
from libs import Card
from libs import Tab

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


        def a():
            lenth = 100
            for x in  range(50):
                self.add_tab(x)
                cont = self.add_container(x)
                print(cont)
                for i in range(lenth):
                    #sleep(1)
                    if self.event.is_set():
                        return
                    sleep(.0001)
                    self.add_card(i, cont)
        #Thread(target=a).start()
        a()
        #self.root.ids.bar.scroll_to(self.root.ids.test)
    def on_stop(self):
        self.event.set()
    #@mainthread
    def add_card(self, i, widget):
        widget.add(Card(text = str(i)))
   # @mainthread
    def add_widget1(self, widget, child):
        widget.add_widget(child)
    #@mainthread
    def add_tab(self, name):
        print(name, type(name))
        tb = Tab(text = str(name))
        self.root.ids.bar_box.add_widget(tb)
   # @mainthread
    def add_container(self, x):
        cont = RContainer()
        print(cont, x)
        scr=scrz(name = str(x))
        self.add_widget1(self.root.ids.scrz_manager, scr)
        scr.add_widget(cont)
        return cont
main=Main()
main.run()