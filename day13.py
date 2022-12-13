import numpy as np

with open("day13test.txt") as f:
    raw = f.read()
    pairs_raw = raw.split("\n\n")

def part1():
    pairs = [[eval(raw_packet) for raw_packet in raw_pair.splitlines()] for raw_pair in pairs_raw]
    print(pairs)
    
    for pair in pairs:
        left_queue = []
        right_queue = []

        left_queue.append(pair[0])
        right_queue.append(pair[1])

        while len(left_queue)>0 or len(right_queue)>0:
            left = left_queue.pop(0)
            

part1()