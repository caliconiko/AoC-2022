from __future__ import annotations
from functools import total_ordering
import numpy as np

with open("day13.txt") as f:
    raw = f.read()
    packets_raw = raw.split()
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

@total_ordering
class Packet:
    def __init__(self, data_list:list) -> None:
        self.data = data_list

    def push_list_to_stacc(stacc_list:list, push_list:list):
        return push_list+[EndOfList()]+stacc_list

    def __repr__(self) -> str:
        return f"{self.data}"

    def __lt__(self, other_right:Packet):
        left_stacc=Packet.push_list_to_stacc([], self.data)
        right_stacc=Packet.push_list_to_stacc([], other_right.data)

        in_the_right_order = False

        while len(left_stacc)>0 or len(right_stacc)>0:
            # print(left_stacc)
            # print(right_stacc)
            # print("---")
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
                left_stacc=Packet.push_list_to_stacc(left_stacc, left)
                right_stacc=Packet.push_list_to_stacc(right_stacc, right)

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
                
                left_stacc=Packet.push_list_to_stacc(left_stacc, left)
                right_stacc=Packet.push_list_to_stacc(right_stacc, right)

        return in_the_right_order

    def __eq__(self, other_right:Packet):
        return self.data == other_right.data

def part2():
    packets_list = [eval(packet_raw) for packet_raw in packets_raw]
    
    divider_packets = [[[2]], [[6]]]
    
    packets_list += divider_packets

    packets = [Packet(packet_list) for packet_list in packets_list]
    packets_sorted = sorted(packets)

    divider_packet_indexes:list[int] = []

    for i, packet in enumerate(packets_sorted):
        if packet.data in divider_packets:
            divider_packet_indexes.append(i+1)

    print(np.product(divider_packet_indexes))

part2()