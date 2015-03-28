#!/usr/bin/env python3


tab = []


with open("test_round.in", "r") as f:
    R, C, H, S = map(int, f.readline().split())
    print("%s %s %s %s" % (R, C, H, S))
    for line in f:
        l = line.replace('\r', '').replace('\n', '')
        print("[%s]" % l)
        tab.append(l)


print(tab)


with open("output.txt", "w") as text_file:
    for s in tab:
        print(s, file=text_file)
