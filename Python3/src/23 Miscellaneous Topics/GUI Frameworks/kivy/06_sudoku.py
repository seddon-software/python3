from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, Line
from kivy.core.window import Window
from kivy.clock import Clock
from functools import partial
import re


initialCells = """
-3-5----4 ----7---- --71-9---
----4---- --5--931- -93-1--46
-8----17- ---6428-3-6-8-----
"""
class Cell(Button):
    cells = []
    def __init__(self, rowsAndCols):
        '''
        for unsolved cells their position is recorded in rowsAndColumns
        for solved cells rowsAndColumns will be empty
        '''
        Cell.cells.append(self)
        super().__init__()
        self.rowsAndCols = rowsAndCols
        if self.rowsAndCols:
            self.solved = False
        else:
            self.solved = True

    def setText(self, text=None):
        '''
        This is called for solved and unsolved cells
        if a cell is solved then text will be non null
        if a cell is unsolved we calculate the text 
        '''
        if not text:                
            rc = self.rowsAndCols
            text = rc['rowC']*3 + rc['colC'] + 1
        self.text = f"{text}"
    
    def on_press(self, *a):
        '''
        Check cell is unsolved, then Toggle text
        '''
        if self.parent.solved: return
        
        if self.text == "":
            self.setText()
        else:
            self.text = ""

class MyGridLayout(GridLayout):
    grids = []
    gridUnderMouse = None
    
    def findGrid(mousePosition):
        x, y = mousePosition
        for grid in MyGridLayout.grids:
            x1 = grid.x
            x2 = grid.x + grid.width
            y1 = grid.y
            y2 = grid.y + grid.height
            if(x1 <= x and x <= x2 and y1 <= y and y <= y2 and grid.level == 3): 
                return grid
        return None

    def mouseOverGrid(instance, mousePosition):
        grid = MyGridLayout.findGrid(mousePosition)
        if grid: 
            MyGridLayout.gridUnderMouse = grid

    def enterNumberInCell(_, keyboard, keycode, text, modifiers):
        '''
        solving this cell: can only be called if level 3 grid is unsolved
        '''        
        try:
            # text must be an int in range 1 to 9
            n = int(text)
            if n == 0: raise Exception()
        except:
            return

        grid = MyGridLayout.gridUnderMouse
        if(grid.solved): return
        grid.solved = True
        
        def createSolvedCell():
            cell = Cell({})
            cell.color = (0,0,0,1)
            cell.font_size = 2 * cell.font_size
            cell.setText(text)
            cell.background_normal = ''
            cell.background_color = (0.8,0.8,0.8,1)
            return cell

        def replaceGridChildrenWithSolvedCell():
            grid.clear_widgets()
            grid.rows = 1
            grid.cols = 1
            grid.add_widget(solvedCell)       

        def adjustUnsolvedCells():
            def isSameRow():
                if grid.rowsAndCols['rowA'] != unsolvedCell.rowsAndCols['rowA']: return False
                if grid.rowsAndCols['rowB'] != unsolvedCell.rowsAndCols['rowB']: return False
                return True
            
            def isSameCol():
                if grid.rowsAndCols['colA'] != unsolvedCell.rowsAndCols['colA']: return False
                if grid.rowsAndCols['colB'] != unsolvedCell.rowsAndCols['colB']: return False
                return True
            
            def isSameSquare():
                if grid.rowsAndCols['rowA'] != unsolvedCell.rowsAndCols['rowA']: return False
                if grid.rowsAndCols['colA'] != unsolvedCell.rowsAndCols['colA']: return False
                return True
            
            app = App.get_running_app()
            root = app.root
            unsolvedCells = [widget for widget in root.walk() if isinstance(widget, Cell) if not widget.solved]
            targetRowA = grid.rowsAndCols['rowA']
            targetColA = grid.rowsAndCols['colA']
            targetRowB = grid.rowsAndCols['rowB']
            targetColB = grid.rowsAndCols['colB']
            for unsolvedCell in unsolvedCells:
                if solvedCell.text == unsolvedCell.text:
                    if isSameRow(): unsolvedCell.text = ""
                    if isSameCol(): unsolvedCell.text = ""
                    if isSameSquare(): unsolvedCell.text = ""
        solvedCell = createSolvedCell()
        replaceGridChildrenWithSolvedCell()
        adjustUnsolvedCells()

    def __init__(self, **kwargs):
        self.level = kwargs.pop('level')
        self.rowsAndCols = kwargs.pop('rowsAndCols')
        super().__init__(**kwargs)
        MyGridLayout.grids.append(self)
        self.solved = False

    def on_center(self, button, pos):
        spacing = ([12, 12], [6,6], [0,0])
        colors  = ([1,1,0,1], [1,0,1,1], [0,1,1,1])
        self.spacing = spacing[self.level - 1]
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*colors[self.level - 1])
            Rectangle(pos=self.pos, size=self.size)

class MyFrame(App):    
    def build(self):
#        Window.size = (1000, 1000)
#        Window.clearcolor = (1, 1, 1, 1)
        self.title = 'Sudoku Solver'

        layout = MyGridLayout(level=1, rows=3, cols=3, rowsAndCols={})
        layout.size = (1000, 1000)
        Window.clearcolor = (0, 0, 0, 1)
        for rowA in range(3):
            for colA in range(3):
                innerLayout1 = MyGridLayout(rows=3, cols=3, level=2, rowsAndCols={'rowA':rowA, 'colA':colA})
                layout.add_widget(innerLayout1)
                for rowB in range(3):
                    for colB in range(3):
                        innerLayout2 = MyGridLayout(rows=3, cols=3, level=3, rowsAndCols={'rowA':rowA, 'colA':colA, 'rowB':rowB, 'colB':colB})
                        innerLayout1.add_widget(innerLayout2)
                        for rowC in range(3):
                            for colC in range(3):
                                cell = Cell({'rowA':rowA, 'colA':colA, 'rowB':rowB, 'colB':colB, 'rowC':rowC, 'colC':colC})
                                cell.setText()
                                innerLayout2.add_widget(cell)
        layout.background_normal = ''
        layout.background_color = (1, 0, 0, 1)
        Window.bind(mouse_pos=MyGridLayout.mouseOverGrid)
        Window.bind(on_key_down=MyGridLayout.enterNumberInCell)
        global initialCells
        Clock.schedule_once(partial(self.populate, initialCells), 1.0)
        return layout

    def populate(self, initialCells, t):
        data = re.sub(r'[\s\n]+', "", initialCells)
        app = App.get_running_app()
        root = app.root
        grids = [widget for widget in root.walk() if isinstance(widget, MyGridLayout) if widget.level == 3]        
        for grid, text in zip(grids, data):
            MyGridLayout.gridUnderMouse = grid
            MyGridLayout.enterNumberInCell(None, None, None, text, None)

                
MyFrame().run()
