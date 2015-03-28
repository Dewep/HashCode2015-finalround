__author__ = 'steven'

from case import Case, Vector

class Balloon(object):
    def __init__(self, _id, current_case, target):
        self.alt = 0
        self.current_case = current_case
        self.movements = []
        self.id = _id
        self.target = target

    def move(self, movement):
        move = 0
        if self.current_case.up == movement:
            move = 1
        if self.current_case.down == movement:
            move = -1
        if self.current_case.next == movement:
            move = 0
        self.movements.append(move)
        self.current_case = movement

    def __str__(self):
        return "alt(%s),  current(%s), movements(%s)" % (self.alt, self.current_case, " ".join(self.movements))

