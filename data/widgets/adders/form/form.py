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
    input_type: "text"
<BaseForm>:
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
        id: first_input
    MyInput:
        id: second_input

    BoxLayout:
        spacing: dp(50)
        FloatLayout:
            size_hint: .5, 1
            MyButton:
                text: "add"
                on_press: root.add()

        FloatLayout:
            size_hint: .5, 1
            MyButton:
                text: "close"
                on_press: root.parent.remove_widget(root)
            
            
  


""")

class MyButton(F.ButtonBehavior, F.Label):
    color = F.ListProperty([0, 0, 0, 1])
    size_hint = F.ListProperty([None, 1])
    width = F.NumericProperty(50)
    pos_hint = {"center_x": .5, "center_y": .5}
class MyInput(F.TextInput):pass

class BaseForm(F.ButtonBehavior, F.BoxLayout):
    def add(self):print("dd")

class FormTab(BaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.remove_widget(self.ids.second_input)
    def add(self):
        print("tab")

class FormCard(BaseForm):pass