#!/usr/bin/env python3
from locator import Locator

from obj import Balloon
from case import Case
import sys
import math
import heapq
targets = []
world = []
balloons = []

sys.setrecursionlimit(1000000)

with open("final_round.in", "r") as f:
    R, C, A = map(int, f.readline().split())
    L, V, B, T = map(int, f.readline().split())
    RS, CS = map(int, f.readline().split())
    max_y = R
    max_x = C
    max_altitude = A
    nb_targets = L
    radius = V
    nb_balloons = B
    nb_tours = T
    start_x = CS
    start_y = RS
    print("max_y=%s max_x=%s max_altitude=%s" % (R, C, A))
    print("nb_targets=%s radius=%s nb_balloons=%s nb_tours=%s" % (L, V, B, T))
    print("start_x=%s start_y=%s" % (start_x, start_y))
    for b in range(0, nb_balloons):
        balloons.append(Balloon(b, None, int(b * max_y / nb_balloons)))
    for i in range(0, L):
        RI, CI = map(int, f.readline().split())
        targets.append((CI, RI))
    for j in range(0, A):
        altitude = []
        for tmp1 in range(0, C):
            tab = []
            for tmp2 in range(0, R):
                tab.append(None)
            altitude.append(tab)
        for y in range(0, R):
            vectors = list(map(int, f.readline().split()))
            index = 0
            x = 0
            while x < C:
                altitude[x][y] = (vectors[index + 1], vectors[index])
                index += 2
                x += 1
        world.append(altitude)


world_cases = []



altitude = 1
world_cases.append([]) # altitude 0
for level in world:
    world_cases.append([])
    for x in range(0, C):
        world_cases[altitude].append([])
        for y in range(0, R):
            world_cases[altitude][x].append(Case(x, y, altitude, world[altitude - 1][x][y]))
    # penser a wrap le monde

    altitude += 1

# fonction d'output

def display_world():
    alt = 0
    for level in world_cases:
        print("Altitude %s" % (alt))
        for x in range(0, C):
            if x < len(world_cases[alt]):
                for y in range(0, R):
                    if y < len(world_cases[alt][x]):
                        print("(x:%s, y:%s): %s" % (x, y, world_cases[alt][x][y]))
        alt += 1


def map_world():
    alt = 0
    for level in world_cases:
        print("Altitude %s" % (alt))
        for x in range(0, C):
            if x < len(world_cases[alt]):
                for y in range(0, R):
                    if y < len(world_cases[alt][x]):
                        obj = world_cases[alt][x][y]
                        obj.next = world_cases[alt][(x + obj.move.x) % max_x][y + obj.move.y] if (y + obj.move.y) < max_y and (y + obj.move.y) >= 0 else None
                        if alt > 1:
                            obj.down = world_cases[alt - 1][x][y]
                        if alt + 1 < max_altitude:
                            obj.up = world_cases[alt + 1][x][y]
        alt += 1

map_world()
#display_world()

def get_dist(visited, actual, target, prev_dist):
    if actual in visited:
        return sys.maxsize
    visited.append(actual)
    #print("actual(%s), target(%s)" % (actual, target))
    #print("Visited: %s" % (str(visited)))
    #if actual.x == target[0] and actual.y == target[1]:
    #    return 0

    unvisited = [] # a prioriser
    if actual.up:
        unvisited.append(actual.up)
    if actual.down:
        unvisited.append(actual.down)
    if actual.next:
        unvisited.append(actual.next)
    current_dist = math.sqrt(math.pow(abs(actual.x - target[0]), 2) + math.pow(abs(actual.y - target[1]), 2))
    #print("current_dist: %s" % current_dist)
    if prev_dist < current_dist:
        return prev_dist
    for item in unvisited:
        new_dist = get_dist(visited, item, target, current_dist)
        if new_dist < current_dist:
            current_dist = new_dist
    return current_dist

def search_path(start, goal):
    node = start
    node.dist = 0
    visited = [start]
    minimum = sys.maxsize
    closest = None
    up_dist = get_dist(visited, node.up, goal, sys.maxsize) if node.up else sys.maxsize
    down_dist = get_dist(visited, node.down, goal, sys.maxsize) if node.down else sys.maxsize
    next_dist = get_dist(visited, node.next, goal, sys.maxsize) if node.next else sys.maxsize
    mini = min(up_dist, down_dist, next_dist)
    print(mini)
    if mini == up_dist:
        return node.up
    if mini == down_dist:
        return node.down
    if mini == next_dist:
        return node.next
    return None

locator = Locator(targets, nb_balloons, radius, max_x, max_y)
best_targets = locator.get_best_targets_list()
print(best_targets)

i = 0
for ballon in balloons:
    #if i == 51:
    ballon.current_case = world_cases[1][start_x][start_y]
    ballon.movements.append(1)
    #else:
    #    ballon.movements.append(0)
    i += 1
# lancer les ballons avant puis imaginer un décalage
for i in range(0, nb_tours):
    print("TOUR=====", i)
    add = False
    #if i < len(balloons) and not balloons[i].current_case:
    #    balloons[i].current_case = world_cases[1][start_x][start_y]
    #    ballon.movements.append(1)
    for ballon in balloons:
        found = False
        if not ballon.current_case:
            ballon.move(None)
            continue
        """for target in targets:
            movement = search_path(ballon.current_case, target)
            print("move: %s" % (movement))
            if movement:
                ballon.move(movement)
                found = True
                break
        if not found:
            print("Damn")
            ballon.move(None)
        """
        objectif_x, objectif_y = locator.get_next_position((ballon.current_case.x, ballon.current_case.y))
        print("OBJECTIF: %s:%s => %s:%s" % (ballon.current_case.x, ballon.current_case.y, objectif_x, objectif_y))
        movement = search_path(ballon.current_case, (objectif_x, objectif_y))
        print("move: %s" % (movement))
        ballon.move(movement)

#print(targets)

"""
from tools import color
for y in range(0, max_y):
    for x in range(0, max_x):
        if (x, y) in targets and (x, y) in best_targets:
            color(3)
        elif (x, y) in targets:
            color(1)
        elif (x, y) in best_targets:
            color(2)
        else:
            color(None)
        print(" ", end="")
    print("")
color(None)
"""

with open("result.txt", "w") as text_file:
    for t in range(0, nb_tours):
        res = []
        for b in balloons:
            if t >= len(b.movements):
                res.append("0")
            else:
                res.append(str(b.movements[t]))
        print(" ".join(res), file=text_file)
