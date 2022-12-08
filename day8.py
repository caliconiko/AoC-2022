from __future__ import annotations
import numpy as np

with open("day8.txt") as f:
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
    pretty_printy(summm)
    print(np.sum(summm[1:-1,1:-1])+(grid.shape[0]-1)*4)

def part2():
    grid = np.array([[int(tree) for tree in list(line)] for line in lines], dtype=np.intc)

    def get_the_of(x:int, y:int, grid:np.ndarray):
        width = grid.shape[0]
        up=grid[0:y, x][::-1]
        down=grid[y+1:width, x]
        left=grid[y, 0:x][::-1]
        right=grid[y, x+1:width]
        dirs = [up, left, down, right]

        current_height = grid[y, x]

        dir_counts = []

        for dir in dirs:
            if np.any(dir>=current_height):
                dir_counts.append(np.argmax(dir >= current_height)+1)
            else:
                dir_counts.append(len(dir))

        return np.product(dir_counts)

    the_ofs = []
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            the_ofs.append(get_the_of(i, j, grid))

    print(np.max(the_ofs))

def pretty_printy(arr):
    for line in arr:
        for c in line:
            if c>0:
                print("#", end="")
            else:
                print(" ", end="")
        print()

part2()