from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

from kivy.uix.button import Button


class MainWidget(Widget):
    pass


# class CanvasExample1(Widget):
#     pass

# class CanvasExample2(Widget):
#     pass

# class CanvasExample3(Widget):
#     pass

# from kivy.graphics.vertex_instructions import Line
# from kivy.graphics.vertex_instructions import Rectangle
# from kivy.graphics.context_instructions import Color
# # make canvas in file
# class CanvasExample4(Widget):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         with self.canvas:
#             Line(points=(0,0,100,200), width=2) # color cann't be use locally
#             Color(0,1,0)
#             # for i in range(10,100,10):
#             #     Color(i/50,i/100,i/400)
#             #     Line(circle=(200,200,50+i))
#             Line(circle=(200,200,50))
#             Line(rectangle=(300,300,50,100), width=2)

#             # To draw filled rectangle
#             self.rect = Rectangle(pos=(300, 50), size=(40,50))
    

# from kivy.metrics import dp    
# from kivy.graphics.vertex_instructions import Rectangle
# from kivy.graphics.context_instructions import Color
# # Move rectangle by clicking the button
# class CanvasExample4_1(Widget):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         with self.canvas:
#             Color(0,1,0)
#             self.rect = Rectangle(pos=(300, 50), size=(40,50))
      
#     def move_rectangle(self):
#         # print("click hua")
#         # x,y = self.rect.pos
#         # x = x+dp(10)
#         # self.rect.pos = (x,y) # yh window cross kr jata h jo hm ni chahte

#         x,y = self.rect.pos
#         w,h = self.rect.size
#         inc=dp(10)        # increment
#         diff = self.width-(x+w)
#         if diff<inc:
#             inc = diff
#         x += inc
#         self.rect.pos = (x,y)    

# from kivy.metrics import dp    
# from kivy.graphics.vertex_instructions import Ellipse
# from kivy.graphics.context_instructions import Color
# from kivy.properties import Clock
# class CanvasExample5(Widget):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.ball_size = dp(50)
#         # Define velocity of ball
#         self.vx = dp(3)
#         self.vy = dp(3)
        
#         with self.canvas:
#             self.ball = Ellipse(pos=(100,100), size=(self.ball_size, self.ball_size))

#         Clock.schedule_interval(self.update, 1/60) # to change the ball pos call update fn 60 per 1 second(60fps)
#     def on_size(self, *args):
#         # print("on_size : "+str(self.width)+", "+str(self.height))
#         self.ball.pos = (self.center_x-self.ball_size/2, self.center_y-self.ball_size/2)

#     def update(self, dt):   # dt = data time
#         # print("update")
#         x,y = self.ball.pos
#         x += self.vx
#         y += self.vy
        
#         # Rebound from top
#         if y+self.ball_size>self.height:
#             y = self.height-self.ball_size
#             self.vy = -self.vy # going to opposite direction
#         # Rebound from right
#         if x+self.ball_size>self.width:
#             x = self.width-self.ball_size
#             self.vx = -self.vx # going to opposite direction
#         # Rebound from bottom
#         if y<0:
#             y=0
#             self.vy = -self.vy
#         # Rebound from left
#         if x<0:
#             x=0
#             self.vx = -self.vx
            
#         self.ball.pos = (x,y)
    
class CanvasExample6(Widget):
    pass

class CanvasExample6_1(Widget):
    pass

from kivy.uix.boxlayout import BoxLayout
class CanvasExample7(BoxLayout):
    pass

class TheLab1App(App):
    pass


TheLab1App().run()
