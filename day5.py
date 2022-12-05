import numpy as np
from collections import defaultdict

with open("day5.txt") as f:
    raw = f.read()
    sections = raw.split("\n\n")

def part1():
    def read_stacks(stacks_raw):
        stacks_lines = stacks_raw.splitlines()

        stacks_nums = stacks_lines[-1]
        stacks_width = (len(stacks_nums)+1)//4

        stacks_height = len(stacks_lines)-1

        all_the_stacks = []
        for i in range(stacks_width):
            current_stack = []
            for j in range(stacks_height):
                crate = stacks_lines[j][i*4+1]
                if crate!=" ":
                    current_stack.insert(0, crate)
            all_the_stacks.append(current_stack)
        return all_the_stacks

    crate_stacks = read_stacks(sections[0])
    instructions = sections[1].splitlines()
    for instruction in instructions:
        ins_split = instruction.split()
        iters = int(ins_split[1])
        stack_from = int(ins_split[3])
        stack_to = int(ins_split[5])

        for i in range(iters):
            picked_up = crate_stacks[stack_from-1].pop()
            crate_stacks[stack_to-1].append(picked_up)
    print("".join([stack[-1] for stack in crate_stacks]))

def part2():
    def read_stacks(stacks_raw):
        stacks_lines = stacks_raw.splitlines()

        stacks_nums = stacks_lines[-1]
        stacks_width = (len(stacks_nums)+1)//4

        stacks_height = len(stacks_lines)-1

        all_the_stacks = []
        for i in range(stacks_width):
            current_stack = []
            for j in range(stacks_height):
                crate = stacks_lines[j][i*4+1]
                if crate!=" ":
                    current_stack.insert(0, crate)
            all_the_stacks.append(current_stack)
        return all_the_stacks

    crate_stacks = read_stacks(sections[0])
    instructions = sections[1].splitlines()
    for instruction in instructions:
        ins_split = instruction.split()
        iters = int(ins_split[1])
        stack_from = int(ins_split[3])
        stack_to = int(ins_split[5])

        temp_stack = []

        for i in range(iters):
            picked_up = crate_stacks[stack_from-1].pop()
            temp_stack.append(picked_up)

        temp_stack=reversed(temp_stack)

        crate_stacks[stack_to-1]+=temp_stack
    print("".join([stack[-1] for stack in crate_stacks]))

part2()