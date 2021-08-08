from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button

from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
class WidgetExample(GridLayout):
    my_text = StringProperty("Hello")
    count = 0
    count_enabled = BooleanProperty(False)
    def on_button_click(self):
        # print("Button Clicked")
        if self.count_enabled:
            self.count +=1
        self.my_text = str(self.count)
    def on_toggle_button_state(self, widget):
        print("toggle state " + widget.state) # widget.state return some character (Down/Normal)
        if widget.state == "normal":
            widget.text='OFF' # OFF
            self.count_enabled = False
        else:
            widget.text='ON' # ON
            self.count_enabled = True

    def on_switch_active(self, widget): # agar .kv me hi kr rhe to iski jrurat nhi
        print("Switch : "+ str(widget.active))
        # hm toggle button ki tarah isme bhi kisi widget ka control
        # kr skte hai

    # Slider ke liye function
    slider_text = StringProperty("50")
    def on_slider_value(self, widget):
        self.slider_text = str(int(widget.value))
        print("Slider Value: "+ str(int(widget.value))) # by default float value hoti hai
    
    # Now Label will update text only on pressing enter key
    text_input = StringProperty("Default")
    def on_text_validate(self, widget):
        self.text_input = widget.text




from kivy.metrics import dp
from kivy.uix.stacklayout import StackLayout
class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation= "lr-tb" # by default
        for i in range(0,100):
            # if we are taking 100 button  then the all button will not accomodate on screen
            # So we will use scrolling
            #size = dp(180)+i*10 # different shape
            sz = dp(100) # sz is just a variable
            b = Button(text = str(i+1), size_hint=(None, None), size=(sz, sz))
            self.add_widget(b)


# With Grid layout we can organize our content 
# in row and column wise
# from kivy.uix.gridlayout import GridLayout
# class GridLayoutExample(GridLayout):
#     pass


from kivy.uix.anchorlayout import AnchorLayout
class AnchorLayoutExample(AnchorLayout):
    pass



from kivy.uix.boxlayout import BoxLayout
class BoxLayoutExample(BoxLayout):
    pass
# Below is one of the method to make a layout button but this not very well
# for each moment so we do same on in .kv file with different syntax

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     b1 = Button(text='A')
    #     b2 = Button(text='B')
    #     b3 = Button(text='C')
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)
        
# Yh by default screen pr horizontally stack krta hai but we can change 

        

class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


TheLabApp().run()
