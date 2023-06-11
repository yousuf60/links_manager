

from kivy.app import App
from kivy.factory import Factory as F
from kivy.clock import mainthread

from libs import (Box,  
                RContainer,
                Card,
                Tab,
                DataManager, #treating with the csv files       
                FormTab,
                FormCard                         
)

from threading import Thread
from threading import Event
import asyncio
from time import sleep
import os


class scrz(F.Screen):pass


class Main(App, DataManager):
    event = Event()
    cont = None
    last_colored_tab = None
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
        
    def on_start(self):
        
        def a():
            
            for x in  self.files_list():
                print(x)
                file = x
                x = os.path.splitext(file)[0]

                self.add_tab(x)
                self.add_container(x)
                
                #waiting the contaner to be added
                while not self.cont:
                    sleep(.02) 
                    if self.event.is_set():
                        return

                for line in self.read(file):
                    if self.event.is_set():
                        return
                    sleep(.001)
                    self.add_card(tuple(line), self.cont)

                self.cont = None
            self.last_colored_tab = self.root.ids.bar_box.children[-1]
            self.last_colored_tab.bakground_coloring()
        Thread(target=a).start()
        #self.root.ids.bar.scroll_to(self.root.ids.test)
    def on_stop(self):
        self.event.set()
    @mainthread
    def add_card(self, i, widget):
        widget.add(Card(i[0], text = str(i[1])))
    @mainthread
    def add_widget1(self, widget, child):
        widget.add_widget(child)
    @mainthread
    def add_tab(self, name):
        print(name, type(name))
        tb = Tab(text = str(name), app = self)
        self.root.ids.bar_box.add_widget(tb)
    @mainthread
    def add_container(self, x):
        self.cont = RContainer()
        scr = scrz(name = str(x))
        scr.on_pre_leave = lambda :self.last_colored_tab.bakground_uncoloring()
        self.add_widget1(self.root.ids.scrz_manager, scr)
        scr.add_widget(self.cont)
    
 
main=Main()
main.run()

