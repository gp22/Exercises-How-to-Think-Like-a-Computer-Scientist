# In games, we often put a rectangular “bounding box” around our sprites
# in the game. We can then do collision detection between, say, bombs and
# spaceships, by comparing whether their rectangles overlap anywhere.
# Write a function to determine whether two rectangles collide.
# Hint: this might be quite a tough exercise! Think carefully about all
# the cases before you code.

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
        
    def contains(self, testPoint):
        hMin = self.lowerLeft.x
        hMax = self.lowerLeft.x + self.width
        vMin = self.lowerLeft.y
        vMax = self.lowerLeft.y + self.height        
        return ((testPoint.x >= hMin) and (testPoint.x <= hMax)) and \
               ((testPoint.y >= vMin) and (testPoint.y <= vMax))

    def collides(self, RectangleB):
        r_B_lowerLeft = 
        r_B_lowerRight =
        r_B_vert_min
        r_B_vert_max
        pass        
        
r = Rectangle(Point(0, 0), 10, 5)
s = Rectangle(Point(0, 0), 10, 5)
print(r.contains(Point(0, 0))) # True
print(r.contains(Point(3, 3))) # True
print(r.contains(Point(3, 7))) # False
print(r.contains(Point(3, 5))) # False
print(r.contains(Point(3, 4.99999))) # True
print(r.contains(Point(-3, -3))) # False