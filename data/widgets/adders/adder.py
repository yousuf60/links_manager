from kivy.lang import Builder
from kivy.factory import Factory as F
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
    y: Window.size[1] - 80

""")

class BaseAdder(F.ButtonBehavior, F.FloatLayout):
    # xy of size >>line 8
    xy = F.NumericProperty(35)

class AddTab(BaseAdder):
    color = [1, 0, 0, 1]
    def on_press(self):
        print('sada')

class AddCard(BaseAdder):
    color = [0, 0,1, 1]
