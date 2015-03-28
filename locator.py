#!/usr/bin/env python3
import math


class Locator(object):
    def __init__(self, targets, nb_balloons, radius, map_x, map_y):
        self.targets = targets
        self.nb_balloons = nb_balloons
        self.radius = radius
        self.map_x = map_x
        self.map_y = map_y

    """ Return a list containing the best spots for our balloons (= covering the most target) """
    def get_best_targets_list(self):
        # CACHE
        # return self._get_best_targets_list()
        return [(96, 30), (100, 17), (109, 6), (173, 12), (96, 6), (170, 25), (93, 43), (270, 31), (167, 4), (252, 17),
                (265, 18), (185, 5), (258, 6), (106, 23), (251, 29), (270, 7), (274, 20), (91, 56), (102, 36),
                (270, 44), (91, 19), (292, 42), (174, 2), (110, 10), (163, 15), (88, 69), (190, 11), (292, 5),
                (260, 25), (288, 52), (111, 2), (246, 13), (89, 6), (165, 29), (100, 4), (87, 32), (171, 18), (192, 5),
                (277, 32), (155, 0), (0, 4), (23, 8), (90, 47), (243, 27), (267, 48), (289, 32), (281, 10), (253, 11),
                (256, 0), (262, 0), (282, 8)]

    def _get_best_targets_list(self):
        best_targets = []
        exclude = []
        targets = self.targets.copy()
        print("targets=", len(targets))
        while len(best_targets) < self.nb_balloons and len(targets) > 0:
            max_pos = None
            max_count = 0
            for x in range(0, self.map_x):
                for y in range(0, self.map_y):
                    if (x, y) in exclude:
                        continue
                    current_count = 0
                    for t in targets:
                        if math.fabs(t[0] - x) <= self.radius and math.fabs(t[1] - y) <= self.radius and self.is_target_covered_by_balloon(t, (x, y)):
                            current_count += 1
                    if current_count > max_count:
                        max_count = current_count
                        max_pos = (x, y)
                    if current_count == 0:
                        exclude.append((x, y))
            if max_pos:
                i = 0
                while i >= 0 and i < len(targets):
                    if self.is_target_covered_by_balloon(targets[i], max_pos):
                        del targets[i]
                        i -= 1
                    i += 1
                print("max_pos=%s nb=%s" % (max_pos, max_count))
                best_targets.append(max_pos)
            else:
                print("None!")
                break
        print("targets=", len(targets))
        return best_targets

    """ function implementing the formula given in the subject to decide whether a balloon (his radius) covers a given position. Either:
        _ A target
        _ Another balloon (to determine whether they overlap each others)
     """
    def is_target_covered_by_balloon(self, target, balloon):
        (target_x, target_y) = target
        (balloon_x, balloon_y) = balloon
        return (math.pow(target_y - balloon_y, 2) + math.pow(self._column_dist(balloon_x, target_x), 2)) < math.pow(self.radius, 2)

    def _column_dist(self, balloon_x, target_x):
        return min(math.fabs(balloon_x - target_x), self.map_x - math.fabs(balloon_x - target_x))

    def get_next_position(self, balloon):
        (balloon_x, balloon_y) = balloon
        best_targets_list = self.get_best_targets_list()
        shortest_distance = 1000000
        shortest_target = None
        for target in best_targets_list:
            distance = (target[0] - balloon_x + self.map_x) % self.map_x
            if 0 < distance < shortest_distance:
                shortest_distance = distance
                shortest_target = target
        return shortest_target
