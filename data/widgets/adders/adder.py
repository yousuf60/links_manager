from kivy.lang import Builder
from kivy.factory import Factory as F

from .form import (
    FormTab,
    FormCard                         
)


Builder.load_string("""

<BaseAdder>:
    pos_hint: {"center_x": .5}
    size_hint: None, None
    size: dp(self.xy), dp(self.xy)

        
    canvas.before:
        Color:
            rgba: self.color
            
        Ellipse:
            size: self.size[0], self.size[1]
            pos: self.pos
    Image:
        source: "data/pic/+.png"
        pos_hint: {"center_x": .5, "center_y": .5}
        pos: root.pos
        size_hint: None, None
        size: dp(20), dp(20)
        
<AddTab>:
    y:self.parent.parent.ids.bar.y - \
    self.parent.parent.ids.bar.height /2 +dp(2) #10 # Window.size[1] - 80

""")


class BaseAdder(F.ButtonBehavior, F.FloatLayout):
    # xy of size >>line 15
    xy = F.NumericProperty(35)


class AddTab(BaseAdder):
    color = [1, 0, 0, 1]

    def on_press(self):
        root = self.parent 
        if not root.adder_here:
            root.add_widget(FormTab())
            #to not add tow widgets in the same time by the user
            root.adder_here = True

class AddCard(BaseAdder):
    color = [0, 0,1, 1]

    def on_press(self):
        root = self.parent 
        if not root.adder_here:
            root.add_widget(FormCard())
            root.adder_here = True
