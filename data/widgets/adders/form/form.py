"""
    putting information of the tab name or link cards
"""

from kivy.lang import Builder
from kivy.factory import Factory as F

Builder.load_string("""

<MyInput@TextInput>:
    padding: dp(20)
    size_hint: 1, None
    height: self.minimum_height
    hint_text: "dd"
    hint_text_color: (1, 1, 1, .8)
    foreground_color: (1, 1, 1, 1)
    background_color: (0, 0, 1, .7)
    multiline: False
    pos_hint: {"center_x": .5}

<Form>:
    size_hint: .8, None
    pos_hint: {"center_x": .5, "center_y": .5}
    orientation: "vertical"
    spacing: dp(10)
    adaptive_height:True
    height: self.minimum_height + 30


    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [0, 0, 15, 15]
    MyInput:
        hint_text: "wqffw"
    MyInput:
        id: ddd
    BoxLayout:
        spacing: dp(50)
        FloatLayout:
            size_hint: .5, 1
            MyButton:
                text: "add"
                on_press: print("sss")

        FloatLayout:
            size_hint: .5, 1
            MyButton:
                text: "close"
            
            
  


""")

class MyButton(F.ButtonBehavior, F.Label):
    color = F.ListProperty([0, 0, 0, 1])
    size_hint = F.ListProperty([None, 1])
    width = F.NumericProperty(50)
    pos_hint = {"center_x": .5, "center_y": .5}
class MyInput(F.TextInput):pass

class Form(F.ButtonBehavior, F.BoxLayout):pass