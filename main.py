import os
#https://kivy.org/doc/stable/guide/environment.html
os.environ["KIVY_IMAGE"] = "pil,sdl2"
os.environ["KIVY_WINDOW"] = "sdl2"

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


dir = "data/tabs/copy"

if not os.path.exists(dir):
    os.mkdir(dir)

dir = "data/tabs/files"

if not os.path.exists(dir):
    os.mkdir(dir)

dir = "data/tabs/copy/files"

if not os.path.exists(dir):
    os.mkdir(dir)

del dir

class scrz(F.Screen):pass


class Main(App, DataManager):
    event = Event()
    cont = None
    last_colored_tab = None
    # important when we add tab if the app is empty
    new_tab = None
    def on_start(self):
        def a():
            listdir = self.files_list()
            for x in  self.read("files/files.csv"):
                x = x[0]
                if x not in listdir:
                    self - ("files/files.csv", [x])
                    continue
                print(x)
                file = x
                x = os.path.splitext(file)[0]
                self.add_tab(x)
                self.add_container(x)
                
                #waiting the container to be added
                self.wait_container()
                # print(self.cont)
                for line in self.read(file):
                    if self.event.is_set():
                        return
                    sleep(.005)
                    self.add_card(tuple(line), self.cont)

                self.cont = None
            self.last_colored_tab = self.root.ids.bar_box.children[-1]
            self.last_colored_tab.bakground_coloring()
        Thread(target=a).start()
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
        scr.container = self.cont
        scr.on_enter = lambda :self.new_tab.bakground_coloring() if self.new_tab else None
        scr.on_pre_leave = lambda :self.last_colored_tab.bakground_uncoloring()
        self.add_widget1(self.root.ids.scrz_manager, scr)
        scr.add_widget(self.cont)
    
    def wait_container(self):
        while not self.cont:
            sleep(.05) 
            if self.event.is_set():
                return
    
 
main=Main()
main.run()

