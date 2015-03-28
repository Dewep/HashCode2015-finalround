#!/usr/bin/env python3

class Locator(Object):
    def __init__(self, targets, nb_balloons):
        self.targets = targets
        self.nb_balloons = nb_balloons
        self.best_targets = []
        self.get_best_targets_list()

    def get_best_targets_list(self):
        self.best_targets.append((1, 1))
        return self.best_targets