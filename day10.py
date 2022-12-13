from __future__ import annotations
import numpy as np

with open("day10.txt") as f:
    raw = f.read()
    lines = raw.splitlines()

def part1():
    global cycle
    cycle = 0
    global x
    x = 1

    global signal_strengths
    signal_strengths = []

    def do_cycle():
        global cycle
        cycle+=1
        if (cycle-20)%40==0:
            signal_strengths.append(cycle*x)

    for line in lines:
        line_split = line.split()
        match line_split[0]:
            case "noop":
                do_cycle()
            case "addx":
                do_cycle()
                do_cycle()
                x+=int(line_split[1])
    print(sum(signal_strengths))

def array_to_chars(arr:np.ndarray):
    charr = np.where(arr>0, "#", ".")
    return "\n".join(["".join(line) for line in charr])

def part2():
    global cycle
    cycle = 0
    global x
    x = 1

    global screen
    screen = np.zeros((6,40))

    def do_cycle():
        global cycle
        cycle+=1
        sprite = np.zeros((1,40))
        sprite[0,x-1:x+2]=1

        x_coords = cycle%40-1
        to_draw = sprite[0, x_coords]
        
        y_coords = (cycle-1)//40
        screen[y_coords, x_coords]=to_draw

    for line in lines:
        line_split = line.split()
        match line_split[0]:
            case "noop":
                do_cycle()
            case "addx":
                do_cycle()
                do_cycle()
                x+=int(line_split[1])

    print(array_to_chars(screen))


part2()