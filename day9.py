from __future__ import annotations
import numpy as np

with open("day9.txt") as f:
    raw = f.read()
    lines = raw.splitlines()


dir_dict = {
    "U":[0,-1],
    "R":[1,0],
    "D":[0,1],
    "L":[-1,0]
}

def part1():
    head = np.zeros(2)
    tail = np.zeros(2)
    
    visited = np.array([[0,0]])

    for _, instruction in enumerate(lines):
        instruction_split = instruction.split()
        dir = np.array(dir_dict[instruction_split[0]])
        

        for _ in range(int(instruction_split[1])):
            head+=dir
            if np.any(np.absolute(head-tail)>1):
                towards_head = np.sign(head-tail)
                tail+=towards_head

                visited=np.append(visited, [tail], 0)
    visited=np.unique(visited, axis=0)

    # print(visited)
    print(len(visited))

def part2():
    visited = np.array([[0,0]])

    number_of_knots = 10
    knots = np.zeros((number_of_knots,2))
    for _, instruction in enumerate(lines):
        instruction_split = instruction.split()
        dir = np.array(dir_dict[instruction_split[0]])
        

        for _ in range(int(instruction_split[1])):
            knots[0]+=dir
            for i in range(len(knots)-1):
                if np.any(np.absolute(knots[i]-knots[i+1])>1):
                    towards_current = np.sign(knots[i]-knots[i+1])
                    knots[i+1]+=towards_current

                    if i+2==number_of_knots:
                        visited=np.append(visited, [knots[-1]], 0)
    
    visited=np.unique(visited, axis=0)

    print(len(visited))
part2()