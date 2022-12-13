import numpy as np

with open("day13.txt") as f:
    raw = f.read()
    pairs_raw = raw.split("\n\n")

class EndOfList:
    def __repr__(self) -> str:
        return "End Of List"

def part1():
    pairs = [[eval(raw_packet) for raw_packet in raw_pair.splitlines()] for raw_pair in pairs_raw]

    def push_list_to_stacc(stacc_list:list, push_list:list):
        return push_list+[EndOfList()]+stacc_list

    index_plus_one_total = 0

    for i, pair in enumerate(pairs):
        left_stacc = []
        right_stacc = []

        left_stacc=push_list_to_stacc(left_stacc, pair[0])
        right_stacc=push_list_to_stacc(right_stacc, pair[1])

        in_the_right_order = False

        while len(left_stacc)>0 or len(right_stacc)>0:
            print(left_stacc)
            print(right_stacc)
            print("---")
            left = left_stacc.pop(0)
            right = right_stacc.pop(0)

            left_type = type(left)
            right_type = type(right)
            left_done = len(left_stacc)<1 or type(left)==EndOfList
            right_done = len(right_stacc)<1 or type(right)==EndOfList

            if left_done and right_done:
                continue
            elif left_done:
                in_the_right_order = True
                break
            elif right_done:
                in_the_right_order = False
                break


            if left_type==list and right_type==list:
                left_stacc=push_list_to_stacc(left_stacc, left)
                right_stacc=push_list_to_stacc(right_stacc, right)

            elif left_type==int and right_type==int:
                if left == right:
                    continue
                else:
                    in_the_right_order=left<right
                    break
            else:
                if left_type==int:
                    left = [left]
                elif right_type==int:
                    right = [right]
                
                left_stacc=push_list_to_stacc(left_stacc, left)
                right_stacc=push_list_to_stacc(right_stacc, right)

        print(in_the_right_order)
        print("========")

        if in_the_right_order:
            index_plus_one_total+=i+1
    print(index_plus_one_total)






part1()