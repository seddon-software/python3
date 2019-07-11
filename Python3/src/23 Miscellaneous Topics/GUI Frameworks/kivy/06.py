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

 
class Cell:
    def __init__(self, button, rowA, colA, rowB, colB, rowC, colC):
        self.button = button
#         self.cell = r * 9 + c
#         self.row = r
#         self.col = c
        self.square = rowA*3 + colA + 1
#         col = row = 1
#         self.key = (r*3+1 == row) and (c*3+1 == col) 
#         self.solved = False
#        self.candidate = (col % 3) + 3*(row % 3) + 1
        b = self.button

#         with b.canvas.before:
#             Color(.5, .5, .5, 1)
#             Line(width = 200)
#             Rectangle(pos=b.pos, size=b.size)

    def setText(self):
        self.button.text = f"{self.square}"

    def getButton(self):
        return self.button
    
class MyFrame(App, BoxLayout):    
    def build(self):
#        Window.size = (1000, 1000)
        
        layout = GridLayout(rows=3, cols=3, padding=0, spacing=12)
        layout.size = (1000, 1000)
        for rowA in range(3):
            for colA in range(3):
                innerLayout1 = GridLayout(rows=3, cols=3, padding=0, spacing=6)
                layout.add_widget(innerLayout1)
                for rowB in range(3):
                    for colB in range(3):
                        innerLayout2 = GridLayout(rows=3, cols=3, padding=0, spacing=0)
                        innerLayout1.add_widget(innerLayout2)
                        for rowC in range(3):
                            for colC in range(3):
                                cell = Cell(Button(), rowA, colA, rowB, colB, rowC, colC)
                                cell.setText()
                                innerLayout2.add_widget(cell.getButton())
        return layout
    
MyFrame().run()
