from __future__ import annotations
from numpy import Infinity, sqrt 
from functools import total_ordering
import numpy as np

with open("day12.txt") as f:
    raw = f.read()
    lines = raw.splitlines()

@total_ordering
class Node:
    def __init__(self, height:int, x:int, y:int) -> None:
        self.height = height
        self.x = x
        self.y = y

        self.connections:list[Node] = []

        self.via:Node = None
        self.distance = Infinity
        self.heuristic = Infinity
        self.explored = False

    def __repr__(self) -> str:
        return f"H{self.height}"

    def __lt__(self, other):
        return self.heuristic < other

    def __eq__(self, other):
        return self.heuristic == other

    def __add__(self, other):
        return self.height+other

    def __radd__(self, other):
        return self.__add__(other)

    def physical_distance_to(self, node:Node):
        return sqrt((node.x-self.x)**2 + (node.y-self.y)**2)

def get_height_from_char(character:str):
    if character=="S":
        return 0
    elif character=="E":
        return 25
    else:
        return ord(character)-ord("a")

def part1():
    characters = [[n for n in l] for l in lines]

    start:Node
    goal:Node

    nodes:list[list[Node]]=[]
    for i, l in enumerate(characters):
        ln = []
        for j, character in enumerate(l):
            new_node = Node(get_height_from_char(character), i, j)
            ln.append(new_node)

            if character=="S":
                start=new_node
            elif character=="E":
                goal=new_node
        nodes.append(ln)

    for i, l in enumerate(nodes):
        for j, n in  enumerate(l):
            
            for d in [-1, 1]:
                should_be_connected:list[Node] = []
                if d+i>=0 and d+i<len(nodes):
                    to_be_connected = nodes[d+i][j]
                    should_be_connected.append(to_be_connected)
                if d+j>=0 and d+j<len(nodes[0]):
                    to_be_connected = nodes[i][d+j]
                    should_be_connected.append(to_be_connected)
                    # n.connections.append(nodes[i][d+j])
                for to_be_connected in should_be_connected:
                    if n.height >= to_be_connected.height-1:
                        n.connections.append(to_be_connected)

    start.distance = 0
    start.heuristic = start.physical_distance_to(goal)

    queue = [start]

    while len(queue)>0:
        current = queue.pop(0)

        to_explore = current.connections
        
        for being_explored in to_explore:
            potential_new_distance = current.distance+2

            if potential_new_distance<being_explored.distance:
                being_explored.via = current
                being_explored.distance = potential_new_distance
                being_explored.heuristic = being_explored.distance+being_explored.physical_distance_to(goal)

                if not being_explored.explored:
                    found = False
                    for i, q in enumerate(queue):
                        if q > being_explored.heuristic:
                            found=True
                            queue.insert(i, being_explored)
                            break

                    if not found:
                        queue.append(being_explored)

    # get path 
    path = []
    
    current_via = goal
    while current_via.via is not None:
        path.append(current_via)
        current_via = current_via.via
    
    print(len(path))

def part2():
    characters = [[n for n in l] for l in lines]

    start:Node
    goal:Node

    a_s:list[Node]=[]

    nodes:list[list[Node]]=[]
    for i, l in enumerate(characters):
        ln = []
        for j, character in enumerate(l):
            new_node = Node(get_height_from_char(character), i, j)
            ln.append(new_node)

            if character=="S":
                start=new_node
            elif character=="E":
                goal=new_node

            if new_node.height==0:
                a_s.append(new_node)
        nodes.append(ln)

    for i, l in enumerate(nodes):
        for j, n in  enumerate(l):
            
            for d in [-1, 1]:
                should_be_connected:list[Node] = []
                if d+i>=0 and d+i<len(nodes):
                    to_be_connected = nodes[d+i][j]
                    should_be_connected.append(to_be_connected)
                if d+j>=0 and d+j<len(nodes[0]):
                    to_be_connected = nodes[i][d+j]
                    should_be_connected.append(to_be_connected)
                    # n.connections.append(nodes[i][d+j])
                for to_be_connected in should_be_connected:
                    if n.height >= to_be_connected.height-1:
                        n.connections.append(to_be_connected)

    path_lengths = []
    for a in a_s:
        start = a
        start.distance = 0
        start.heuristic = start.physical_distance_to(goal)

        queue = [start]

        while len(queue)>0:
            current = queue.pop(0)

            to_explore = current.connections
            
            for being_explored in to_explore:
                potential_new_distance = current.distance+2

                if potential_new_distance<being_explored.distance:
                    being_explored.via = current
                    being_explored.distance = potential_new_distance
                    being_explored.heuristic = being_explored.distance+being_explored.physical_distance_to(goal)

                    if not being_explored.explored:
                        found = False
                        for i, q in enumerate(queue):
                            if q > being_explored.heuristic:
                                found=True
                                queue.insert(i, being_explored)
                                break

                        if not found:
                            queue.append(being_explored)

    # get path 

    
        path = 0
        
        current_via = goal
        while current_via.via is not None and current_via.via is not start:
            path+=1
            current_via = current_via.via
        path+=1
        
        path_lengths.append(path)
    print(np.min(path_lengths))

part2()