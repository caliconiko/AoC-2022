import numpy as np
from collections import defaultdict

from time import time

with open("day1.txt") as f:
    raw = f.read()
    elves = [np.sum([int(cal) for cal in elf.split("\n") if len(cal)>1]) for elf in raw.split("\n\n")]

print(np.sum(np.sort(elves)[-1::-1][0:3]))