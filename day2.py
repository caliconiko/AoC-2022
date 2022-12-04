import numpy as np
from collections import defaultdict



def letter_to_value(letter):
    letter_to_value_dict = {
        "A":0,
        "B":1,
        "C":2,
        "X":0,
        "Y":1,
        "Z":2
    }
    return letter_to_value_dict[letter]

def calculate_match_result(opponent, you):
    if letter_to_value(opponent) == letter_to_value(you):
        return 0
    elif (letter_to_value(opponent)-1)%3 == letter_to_value(you):
        return -1
    elif (letter_to_value(opponent)+1)%3 == letter_to_value(you):
        return 1

def calculate_match_score(opponent, you):
    match_outcome = calculate_match_result(opponent, you)
    you_letter_value = letter_to_value(you)

    return you_letter_value+1+(match_outcome+1)*3

def part1():
    with open("day2.txt") as f:
        raw = f.read()
        scores = [calculate_match_score(line.split()[0], line.split()[1]) for line in raw.splitlines()]

    print(sum(scores))

def calculate_match_end(opponent, ending):
    opponent_value = letter_to_value(opponent)
    ending_value = letter_to_value(ending)

    ending_shape = (opponent_value+(ending_value-1))%3

    return ending_shape

def calculate_match_end_score(opponent, ending):
    ending_shape = calculate_match_end(opponent, ending)

    return ending_shape+1 + letter_to_value(ending)*3

def part2():
    with open("day2.txt") as f:
        raw = f.read()
        scores = [calculate_match_end_score(line.split()[0], line.split()[1]) for line in raw.splitlines()]
    print(np.sum(scores))

part2()