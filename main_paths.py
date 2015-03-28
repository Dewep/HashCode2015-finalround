#!/usr/bin/env python3
from locator import Locator

from obj import Balloon
from case import Case
import sys
import math
import heapq
from copy import copy

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
        balloons.append(Balloon(b, None, 3 + int(b * (max_y - 6) / nb_balloons)))
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

def search_path(ballon):
    #ballon.target
    y_next = ballon.current_case.next.y if ballon.current_case.next else 1000
    y_up = ballon.current_case.up.next.y if ballon.current_case.up and ballon.current_case.up.next else 1000
    y_down = ballon.current_case.down.next.y if ballon.current_case.down and ballon.current_case.down.next else 1000
    dist_next = abs(ballon.target - y_next)
    dist_down = abs(ballon.target - y_down)
    dist_up = abs(ballon.target - y_up)
    result = min(dist_next, dist_down, dist_up)
    print("result: %s, ballon.id: %s, ballon.target: %s" % (result, ballon.id, ballon.target))
    print("dist_next(%s), dist_down(%s), dist_up(%s)" % (dist_next, dist_down, dist_up))
    if dist_next == result:
        return ballon.current_case
    if dist_down == result:
        return ballon.current_case.down
    if dist_up == result:
        return ballon.current_case.up
    if ballon.current_case.next.y >= 0 or ballon.current_case.next.y < max_y:
        return ballon.current_case
    if ballon.current_case.down.next.y >= 0 or ballon.current_case.down.next.y < max_y:
        return ballon.current_case.down
    if ballon.current_case.up.next.y >= 0 or ballon.current_case.up.next.y < max_y:
        return ballon.current_case.up
    return None

i = 0
for ballon in balloons:
    if i == 2:
        ballon.current_case = copy(world_cases[1][start_x][start_y])
        ballon.movements.append(1)
    else:
        ballon.movements.append(0)
    print("%s : target: %s" % (i, ballon.target))
    i += 1
# lancer les ballons avant puis imaginer un décalage
print(balloons)


for i in range(0, nb_tours):
    for ballon in balloons:
        found = False
        if not ballon.current_case:
            continue
        print("ROUND   ---- %s " % (i))
        print("avant de bouger: ballon %s" % (ballon.current_case))
        movement = search_path(ballon)
        print("move: %s" % (movement))
        if movement:
            ballon.move(movement)
#print(targets)

locator = Locator(targets, nb_balloons, radius, max_x, max_y)
print(locator.get_best_targets_list())

with open("result.txt", "w") as text_file:
    for t in range(0, nb_tours):
        res = []
        for b in balloons:
            if t >= len(b.movements):
                res.append("0")
            else:
                res.append(str(b.movements[t]))
        print(" ".join(res), file=text_file)
