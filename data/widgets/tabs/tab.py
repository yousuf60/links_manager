from kivy.lang import Builder 
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.factory import Factory as F
from kivy.animation  import Animation

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


class Tab(F.ButtonBehavior, F.BoxLayout):
    text = StringProperty("Tab")
    color = ListProperty([0, 0, 0, 0])
    DURATION = .3
    def __init__(self, text = "", app = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if text:
            self.text = str(text)
        if app:
            self.app = app
    def on_press(self):
        #scroll view widget
        scroller =self.parent.parent
        #root float widget
        root = scroller.parent.parent

        scroller.scroll_to(self)
        root.ids.scrz_manager.current = self.text
        self.bakground_coloring()

        #to uncolore it when switching screens
        print(self.app.last_colored_tab)
        self.app.last_colored_tab = self

    def bakground_coloring(self, color = (1, 1, 1, .3)):
        color_animation = F.Animation(color = color, duration = self.DURATION)
        color_animation.start(self)
    def bakground_uncoloring(self, color = (0, 0, 0, 0)):
        color_animation = F.Animation(color = color, duration = self.DURATION)
        color_animation.start(self)
    


