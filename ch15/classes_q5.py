# Write a transpose method in the Rectangle class that swaps the width
# and the height of any rectangle instance:
# r = Rectangle(Point(100, 50), 10, 5)
# test(r.width, 10)
# test(r.height, 5)
# r.transpose()
# test(r.width, 5)
# test(r.height, 10)

import math

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY
        
    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y
        
    def move(self, dX, dY):
        """ move point object dX, dY units. """
        self.x += dX
        self.y += dY

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
        
    def distanceFromPoint(self, point):
        horiz_diff = self.getX() - point.getX()
        vert_diff = self.getY() - point.getY()
        return math.sqrt((horiz_diff ** 2) + (vert_diff ** 2))
    
    def reflect_x(self):
        return Point((self.x * (-1)), self.y)
        
class Rectangle:
    """ Class for representing a rectangle on an x,y grid. """
    
    def __init__(self, lowerLeft, width, height):
        """ Create a new rectangle with lower left corner "lowerLeft" as a 
            Point object, and width and height as the given values. """
        self.lowerLeft = lowerLeft
        self.width = width
        self.height = height

    def __str__(self):
        return 'lowerLeft: (x=' + str(self.lowerLeft.x) + \
                ', y=' + str(self.lowerLeft.y) + ")," + \
                ' width=' + str(self.width) + ', height=' + str(self.height)
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def getLowerLeft(self):
        return ((self.lowerLeft.x), (self.lowerLeft.y))
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return (self.width * 2) + (self.height * 2)
        
    def transpose(self):
        temp = self.width
        self.width = self.height
        self.height = temp

r = Rectangle(Point(100, 50), 10, 5)
print(r.getWidth())
print(r.getHeight())
r.transpose()
print(r.getWidth())
print(r.getHeight())