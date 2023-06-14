# we should make Box contain only two cards
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.widget import Widget
from data.widgets.boxcontainer import Box

Builder.load_string("""
<RContainer>:
    padding: "10dp"
    BoxLayout:
        spacing: "5dp"
        size_hint_y: None
        adaptive_height: True
        id: links_list
        height: self.minimum_height
        orientation: "vertical"
        Widget:
            exists: False
        Widget:
            exists: False
""")


class RContainer(RecycleView):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.lst = self.ids.links_list


    def add(self,w):
        
        child = self.lst.children[-2]
  

        if not child.exists:
            self.make_child(w)
            
        else:
            if child.wgs == 2:
                child.ex()
            if child.wgs < 2:
                child.add_widget(w)
                child.wgs += 1  
            else:
                self.make_child(w)

    def make_child(self, w):
        box = Box()
        box.add_widget(w)
        box.wgs += 1 
        
        self.lst.add_widget(box, index = -1)
               
    

