import numpy as np
from collections import defaultdict

with open("day3.txt") as f:
    raw = f.read()
    lines = raw.splitlines()

def part1():
    def get_priority(item):
        if ord(item) in range(97, 123):
            return ord(item)-96
        else:
            return ord(item)-65+27

    prios = []
    for line in lines:
        first = line[:len(line)//2]
        second = line[len(line)//2:]
        break_it = False
        for l1 in first:
            for l2 in second:
                if l1 == l2:
                    prios.append(get_priority(l1))
                    break_it = True
                    break
            if break_it:
                break

    print(sum(prios))

def part2():
    def get_priority(item):
        if ord(item) in range(97, 123):
            return ord(item)-96
        else:
            return ord(item)-65+27

    prios = []
    for i in range(len(lines)//3):
        group = [list(line) for line in lines[i*3:(i+1)*3]]
        badge = np.intersect1d(group[2],np.intersect1d(group[0], group[1]))[0]
        prios.append(get_priority(badge))

    print(sum(prios))

part2()