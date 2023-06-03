from kivy.lang import Builder
from kivy.factory import Factory as F

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

    def __init__(self,link, color = (), text = "", *args, **kwargs):
        super().__init__(*args, **kwargs)
        if color:
            self.ids.lbl.color = color
        if text:
            self.ids.lbl.text = text
        self.link = link

    def on_press(self):
        print(self.link)