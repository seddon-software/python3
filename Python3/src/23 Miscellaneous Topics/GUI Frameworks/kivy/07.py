from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, Line
from kivy.graphics import *
from kivy import *
from kivy.clock import Clock
from functools import partial
import numpy as np

class MyFrame(App, BoxLayout):    
    def build(self):
        def my_callback(b1, b2, dt):
            print(dt, b1.x, b1.y, b2.x, b2.y)
            b2.border = (10,10,10,10)
            b2.background_normal = ''
            b2.background_color = (1, .3, .4, .85)
#             with b2.canvas:
#                 Color(1, 1, 0, 1)
#                 pos = np.array(b2.pos)
#                 size = np.array(b2.size)
#                 Rectangle(pos=pos + size * 0.05, size=size * 0.9)
            
        Builder.load_file('widgetst.kv')
        
        layout = BoxLayout(spacing=10, orientation='horizontal')
        button1 = Button(text='Hello', pos_hint={'x':.2, 'y':.3}, size_hint=(.7, .8))
        button2 = Button(text='World', size_hint=(.3, 1))
        
        layout.add_widget(button1)
        layout.add_widget(button2)
        Clock.schedule_once(partial(my_callback, button1, button2), -1)

        return layout


MyFrame().run()
