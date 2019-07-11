from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window
 
Builder.load_string("""
<KivyButton>:
    Button:
        pos: 100, 200
        size: 400, 400
        background_normal: ''
        background_color: 0, 1, 0, .85
        text: "-Hello-Button-"
        canvas.before:
            Color:
                rgba: 0, 0, 0, 1
            Line:
                width: 2
                rectangle: self.x, self.y, self.width, self.height
        border: (10,10,10,10)
        Image:
            border: (10,10,10,10)
            background_color: 0, 1, 1, .85
            size: 200, 200
            source: 'images.jpg'
            size_hint: 2.5, 2.5
            center_x: self.parent.center_x 
            center_y: self.parent.center_y  
        Button:
            size: 200, 200
    
""")
 
class KivyButton(App, BoxLayout):
    
    def build(self):
        Window.size = (800, 500)
        return self
    
KivyButton().run()
