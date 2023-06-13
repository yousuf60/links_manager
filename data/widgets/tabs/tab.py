from kivy.app import App 
from kivy.lang import Builder 
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.factory import Factory as F
from kivy.animation  import Animation
from kivy.clock import mainthread

from ..long_press import LongPress
from ...data_lib import DataManager

data_manager = DataManager()

Builder.load_string("""
<Tab>:
    size_hint: None, 1
    adaptive_width: True
    width: self.minimum_width
    padding: dp(len(self.text) * 5 + 15), 0
    canvas:
        Color:
            rgba: self.color
    
        Rectangle:
            size: self.size[0], self.size[1]
            pos: self.pos
   
    Label:
        id: lbl
        text: self.parent.text 
        color: 1, 1, 1, 1
""")


class Tab(F.ButtonBehavior, F.BoxLayout, LongPress):
    text = StringProperty("Tab")
    color = ListProperty([0, 0, 0, 0])
    DURATION = .3
    def __init__(self, text = "", app = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if text:
            self.text = str(text)
        if app:
            self.app = app
            app.new_tab = self
    def on_press(self):
        self.pressed_btn()

    def on_release(self):
        if self.on_release_limit():
            #scroll view widget
            scroller =self.parent.parent
            #root float widget
            root = scroller.parent.parent
            scroller.scroll_to(self)
            root.ids.scrz_manager.current = self.text
            self.bakground_coloring()
            self.new_tab = None
            



    def bakground_coloring(self, color = (1, 1, 1, .3)):
        color_animation = F.Animation(color = color, duration = self.DURATION)
        color_animation.start(self)
        #to uncolore it when switching screens
        self.app.last_colored_tab = self
        self.app.new_tab = None

        
    def bakground_uncoloring(self, color = (0, 0, 0, 0)):
        color_animation = F.Animation(color = color, duration = self.DURATION)
        color_animation.start(self)

    @mainthread
    def remove_self(self):
        self.parent.remove_widget(self)
        app = App.get_running_app()
        screen_manager = app.root.ids.scrz_manager
        screen = screen_manager.get_screen(self.text)
        screen_manager.remove_widget(screen)
        current = screen_manager.current
        for child in app.root.ids.bar_box.children:
            if current == child.text :
                child.bakground_coloring()
    def delete_data(self):
        data_manager.delete_file(self.text + ".csv")
        


