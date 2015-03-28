__author__ = 'steven'

class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(x: %x, y: %s)" % (self.x, self.y)


class Case(object):
    def __init__(self, x, y, altitude, tup):
        self.x = x
        self.y = y
        self.alt = altitude
        self.move = Vector(tup[0], tup[1])
        self.up = None
        self.down = None
        self.next = None

# penser à wrapper la map


