from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.factory import Factory as F

Builder.load_string("""
<Box>:
    orientation: 'horizontal'
    size_hint: 1, None
    height: "80dp"
    spacing: "10dp"


""")

class Box(BoxLayout):
    wgs = 0
    exists = True
    def ex(self):
        self.exists = False