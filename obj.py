__author__ = 'steven'

from case import Case, Vector
from copy import copy

class Balloon(object):
    def __init__(self, _id, current_case, target=0):
        self.alt = 0
        self.current_case = current_case
        self.movements = []
        self.id = _id
        self.target = target

    def move(self, movement):
        move = -42
        if self.current_case.up == movement:
            move = 1
        if self.current_case.down == movement:
            move = -1
        if self.current_case == movement:
            move = 0
        self.movements.append(move)
        self.current_case = copy(movement.next)

    def move2(self, move):
        self.alt += move
        self.movements.append(move)

    def __str__(self):
        return "alt(%s),  current(%s), movements(%s)" % (str(self.alt), self.current_case, " ".join(self.movements))

