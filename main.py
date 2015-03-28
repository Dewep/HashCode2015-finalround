#!/usr/bin/env python3


targets = []
world = []


with open("final_round.in", "r") as f:
    R, C, A = map(int, f.readline().split())
    L, V, B, T = map(int, f.readline().split())
    RS, CS = map(int, f.readline().split())
    max_y = R
    max_x = C
    max_altitude = A
    nb_targets = L
    radius = V
    nb_ballons = B
    nb_tours = T
    start_x = CS
    start_y = RS
    print("max_y=%s max_x=%s max_altitude=%s" % (R, C, A))
    print("nb_targets=%s radius=%s nb_ballons=%s nb_tours=%s" % (L, V, B, T))
    print("start_x=%s start_y=%s" % (start_x, start_y))
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


#print(world)
print(targets)

#with open("output.txt", "w") as text_file:
#    for s in tab:
#        print(s, file=text_file)
