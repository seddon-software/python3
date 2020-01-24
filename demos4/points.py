class Point():
    count = 0
    def getCount():
        return Point.count
    
    def __init__(self, x0, y0, name):
        Point.count += 1
        self.x = x0
        self.y = y0
        self.name = name
        
    def moveBy(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
    
    def display(self):
        print(f"{self.name} is at ({self.x},{self.y})")
        
########################


print(Point.getCount())
p1 = Point(100, 200, 'point-p1')
p2 = Point(150, 250, 'point-p2')
p3 = Point(170, 220, 'point-p3')
p1.count = p1.count
print(p1.__dict__)
print(Point.__dict__)

p1.moveBy(1, 1)
p2.moveBy(10, 15)
p3.moveBy(13, 17)

p1.display()
p2.display()
p3.display()

1  