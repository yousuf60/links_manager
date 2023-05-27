from kivy.lang import Builder 
from kivy.properties import StringProperty
from kivy.factory import Factory as F
Builder.load_string("""
<Tab>:
    size_hint: None, 1
    width: "50dp"
    padding: "10dp"
    Label:
        text: self.parent.text 
        color: 1, 1, 1, 1
""")


class Tab(F.ButtonBehavior, F.BoxLayout):
    text = StringProperty("Tab")
    screen = StringProperty("dd")
    def __init__(self, text = "", screen = "", *args, **kwargs):
        super().__init__(*args, **kwargs)
        if text:
            self.text = StringProperty(str(text))
        if screen:
            self.screen = StringProperty(str(screen))
    def on_press(self):
        x =self.parent.parent 
        x.scroll_to(self)
        x.parent.parent.ids.scrz_manager.current = self.screen
        print(self.parent.parent.parent.parent.ids.scrz_manager.current)

