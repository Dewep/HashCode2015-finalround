#!/usr/bin/env python3
import math


class Locator(object):
    def __init__(self, targets, nb_balloons, radius, map_x, map_y):
        self.targets = targets
        self.nb_balloons = nb_balloons
        self.radius = radius
        self.map_x = map_x
        self.map_y = map_y
        self.best_targets = []

    """ Return a list containing the best spots for our balloons (= covering the most target) """
    def get_best_targets_list(self):
        self.best_targets.append((1, 1))
        return self.best_targets

    """ function implementing the formula given in the subject to decide whether a balloon (his radius) covers a given position. Either:
        _ A target
        _ Another balloon (to determine whether they overlap each others)
     """
    def is_target_covered_by_balloon(self, target, balloon, nb_columns):
        (target_x, target_y) = target
        (balloon_x, balloon_y) = balloon
        return (math.pow(target_y - balloon_y, 2) + math.pow(self._column_dist(balloon_x, target_x, nb_columns), 2)) < math.pow(self.radius, 2)

    def _column_dist(self, balloon_x, target_x, nb_columns):
        return min(math.fabs(balloon_x - target_x), nb_columns - math.fabs(balloon_x - target_x))