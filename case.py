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

    def aff_simple(self):
        return "x(%s), y(%s), alt(%s)" % (self.x, self.y, self.alt)

    def __str__(self):
        return "x(%s), y(%s), alt(%s), vector(%s), up(%s), down(%s), next(%s)" % (self.x, self.y, self.alt, self.move,
                                                                                  self.up.aff_simple() if self.up else None,
                                                                                  self.down.aff_simple() if self.down else None,
                                                                                  self.next.aff_simple() if self.next else None)

# penser à wrapper la map


