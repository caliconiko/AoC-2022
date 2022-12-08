from __future__ import annotations
import numpy as np

with open("day8test.txt") as f:
    raw = f.read()
    lines = raw.splitlines()

def part1():
    grid = np.array([[int(tree) for tree in list(line)] for line in lines], dtype=np.intc)
    
    summm = np.zeros_like(grid)
    for i in range(4):
        hhh=np.array([[np.max(line[0:i+1]) for i in np.arange(grid.shape[0])] for line in grid])
        hhh_pad = np.pad(hhh, 1, constant_values=0)
        hhh_rol = np.roll(hhh_pad, 1, 1)
        ggg_pad = np.pad(grid, 1, constant_values=0)
        un = np.array(ggg_pad>hhh_rol, np.intc)[1:-1,1:-1]
        # print(un)
        for _ in range(4-i):
            un = np.rot90(un)
        summm = np.bitwise_or(un, summm)
        grid=np.rot90(grid)
    # print(np.array([[np.max(line[0:i+1]) for i in np.arange(grid.shape[0])] for line in grid]))
    # print(grid)
    # pretty_printy(summm)   
    print(np.sum(summm[1:-1,1:-1]))

def pretty_printy(arr):
    for line in arr:
        for c in line:
            if c>0:
                print("#", end="")
            else:
                print(" ", end="")
        print()

part1()