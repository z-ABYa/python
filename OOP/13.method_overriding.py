class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def area(self):
        return self.x * self.y
    
class Circle(Rectangle):
    def __init__(self, rad):
        self.rad = rad

    def area(self):#Method over-ridden from parent calss
        super().__init__(self.rad, self.rad)
        return super().area() * 3.14
    
c = Circle(5)
print(c.area())