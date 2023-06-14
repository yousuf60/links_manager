"""
    putting information of the tab name or link cards
"""
from kivy.app import App   
from kivy.lang import Builder
from kivy.clock import mainthread
from kivy.factory import Factory as F
from kivy.core.window import Window
from kivy.properties import StringProperty
from threading import Thread
from time import sleep

from ....data_lib import DataManager

data_manager = DataManager()

Builder.load_string("""
<MyButton>:
    pos_hint: {"center_x": .5, "center_y": .5}

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
        hint_text: root.first_input_hint_text
        foreground_color: root.first_input_foreground_color
        id: first_input
    MyInput:
        hint_text: root.second_input_hint_text
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
                on_press: root.close()
                
            
            
<FormCard@BaseForm>:
    first_input_hint_text: "Name: " + str(int(Window.width) //19) + " character"
    first_input_foreground_color: (1, 1, 1, 1) if len(root.ids.first_input.text) <= int(Window.width) //19 else (1, 0, 0, 1)

<TabCard@BaseForm>:
    first_input_foreground_color: (1, 1, 1, 1)
""")

class MyButton(F.ButtonBehavior, F.Label):
    color = F.ListProperty([0, 0, 0, 1])
    size_hint = F.ListProperty([None, 1])
    width = F.NumericProperty(60)
    
    
class MyInput(F.TextInput):pass

class BaseForm(F.ButtonBehavior, F.BoxLayout):
    second_input_hint_text = StringProperty("Link")
    first_input_hint_text = StringProperty("Name")
    first_input_foreground_color = F.ListProperty([1, 1, 1, 1])
    def close(self):
        self.parent.adder_here = False
        self.parent.remove_widget(self)

class FormTab(BaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.remove_widget(self.ids.second_input)

    def add(self):
        tab_name = self.ids.first_input.text

        if tab_name:
            app = App.get_running_app()
            if self.tab_text_checker(tab_name, app):
                return
            app.add_container(tab_name)
            app.add_tab(tab_name)
            data_manager.make_file(tab_name)

            self.close()



    def tab_text_checker(self, tab_name, app):
        for tab in app.root.ids.bar_box.children:
            if tab.text == tab_name:
                return True
        return False
class FormCard(BaseForm):
    # first_input_hint_text = StringProperty("Name: " + str(int(Window.width) //19) + " character")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.ids.first_input.hint_text = 
    def add(self):
        card_name = self.ids.first_input.text
        link = self.ids.second_input.text
        screen_manager = self.parent.parent.ids.scrz_manager
        current_screen = screen_manager.current
        card_text_length = int(Window.width) //19
        is_right_limit = len(card_name) <= card_text_length
        if all([link, card_name, current_screen, is_right_limit]):
            if self.data_checker(link, card_name, current_screen):
                return 
            app = App.get_running_app()
            data_manager.add(current_screen + ".csv", ((link, card_name), ))
            self.close()
            container = screen_manager.get_screen(current_screen).container
            app.add_card((link, card_name), container)
    def data_checker(self, link, name, file):
        if [link, name] in data_manager.read(file + ".csv"):
            return True 