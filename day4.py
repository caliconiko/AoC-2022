import numpy as np
from collections import defaultdict

with open("day4.txt") as f:
    raw = f.read()
    lines = raw.splitlines()

def part1():
    pairs = [[[int(section) for section in elf.split("-")] for elf in line.split(",")] for line in lines]

    def check_contain_the_other(elf1, elf2):
        return ((elf1[0] >= elf2[0]) and (elf1[0] <= elf2[1])) and ((elf1[1] >= elf2[0]) and (elf1[1] <= elf2[1])) 

    checks = [check_contain_the_other(pair[0], pair[1]) or check_contain_the_other(pair[1], pair[0]) for pair in pairs]
    print(np.sum(checks))

def part2():
    pairs = [[[int(section) for section in elf.split("-")] for elf in line.split(",")] for line in lines]

    def check_contain_the_other(elf1, elf2):
        return ((elf1[0] >= elf2[0]) and (elf1[0] <= elf2[1])) or ((elf1[1] >= elf2[0]) and (elf1[1] <= elf2[1])) 

    checks = [check_contain_the_other(pair[0], pair[1]) or check_contain_the_other(pair[1], pair[0]) for pair in pairs]
    print(np.sum(checks))

part2()