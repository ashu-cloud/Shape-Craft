# this is the python file which has the capability to make all the shapes
# every shape has thier own defined class
from canvaspainter import Canvas
class Rectangle:
    def __init__(self, x,y, length, width, color):
        self.x=x
        self.y=y
        self.length= length
        self.width= width
        self.color = color

    def draw(self , canvas):
        canvas.data[self.x: self.x+ self.length, self.y: self.y+self.width]= self.color
        


class Square:
    def __init__(self, x, y, sidelength, color ):
        self.x=x
        self.y=y
        self.sidelength= sidelength
        self.color= color


    def draw(self, canvas):
        canvas.data[self.x: self.x+ self.sidelength, self.y: self.y+self.sidelength]= self.color

class Circle:
    def __init__(self, center_x, center_y,radius, color):
        self.center_x= center_x
        self.center_y= center_y
        self.radius= radius
        self.color= color


    def draw(self,canvas):
        for x in range(canvas.data.shape[0]):
            for y in range(canvas.data.shape[1]):
                # Check if the point (x, y) lies within the circle
                if (x - self.center_x) ** 2 + (y - self.center_y) ** 2 <= self.radius ** 2:
                    canvas.data[x, y] = self.color