import numpy as np
from collections import defaultdict

with open("day6test.txt") as f:
    raw = f.read()
    lines = raw.splitlines()

def part1():
    stream = lines[0]
    stream_length = len(stream)
    window_size = 4

    for i in range(stream_length-window_size+1):
        window = stream[i:i+window_size]
        if len(np.unique(list(window)))==window_size:
            print(i+window_size)
            break

def part2():
    stream = lines[0]
    stream_length = len(stream)
    window_size = 14

    for i in range(stream_length-window_size+1):
        window = stream[i:i+window_size]
        if len(np.unique(list(window)))==window_size:
            print(i+window_size)
            break

part2()