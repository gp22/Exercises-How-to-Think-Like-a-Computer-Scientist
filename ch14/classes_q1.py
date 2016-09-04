# Add a distanceFromPoint method that works similar to distanceFromOrigin 
# except that it takes a Point as a parameter and computes the distance 
# between that point and self.

import math

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
        
    def distanceFromPoint(self, point):
        horiz_diff = self.getX() - point.getX()
        vert_diff = self.getY() - point.getY()
        return math.sqrt((horiz_diff ** 2) + (vert_diff ** 2))

p = Point(7, 6)
q = Point(36, 19)
print(p.distanceFromPoint(q))
