__author__ = 'steven'

from case import Case, Vector

class Balloon(object):
    def __init__(self):
        self.alt = 0
        self.current_case = None
        self.movements = []

    def move(self, movement): #+1, -1, 0
        self.movements.append(movement)
        #deplacer a la case suivante.

    def __str__(self):
        return "alt(%s),  current(%s), movements(%s)" % (self.alt, self.current_case, " ".join(self.movements))

