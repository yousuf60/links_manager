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
    def __init__(self, text = "", *args, **kwargs):
        super().__init__(*args, **kwargs)
        if text:
            self.text = str(text)
    def on_press(self):
        x =self.parent.parent 
        x.scroll_to(self)
        x.parent.parent.ids.scrz_manager.current = self.text
        print(self.parent.parent.parent.parent.ids.scrz_manager.current)

