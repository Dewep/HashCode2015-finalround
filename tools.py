#!/usr/bin/env python3


def color(nb=None):
    # None: rest, 1:red, 2:yellow, 3:blue, 4:purple, 5:cyan, 6:white
    if nb:
        print("\033[;" + str(40 + nb) + "m")
    else:
        print("\033[0;0m")

