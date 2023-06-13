from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory as F
from kivy.clock import mainthread

from webbrowser import open

from ...data_lib import DataManager
from ..long_press import LongPress

data_manager = DataManager()

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


class Card(F.ButtonBehavior, F.BoxLayout, LongPress):

    def __init__(self,link, color = (), text = "", *args, **kwargs):
        super().__init__(*args, **kwargs)
        if color:
            self.ids.lbl.color = color
        if text:
            self.ids.lbl.text = self.text = text
        self.link = link

    
    def on_press(self):
        self.pressed_btn()

    def on_release(self):
        if self.on_release_limit():
            open(self.link)

    @mainthread
    def remove_self(self):
        self.parent.remove(self)
    def delete_data(self):
        app = App.get_running_app()
        file = app.root.ids.scrz_manager.current + ".csv"
        data_to_delete = (file, self.link, self.text)
        data_manager - data_to_delete
