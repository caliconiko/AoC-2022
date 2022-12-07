from __future__ import annotations
import numpy as np

with open("day7.txt") as f:
    raw = f.read()
    lines = raw.splitlines()

class Node:
    directories:list[Node] = []

    def __init__(self, name:str, parent:Node, size=0) -> None:
        self.children = {}
        self.name = name
        self.size:int = size
        self.parent:Node = parent

        self.computed_size:int = -1

        if size == 0:
           Node.directories.append(self)

    def add_child(self, name:str, size=0):
        new_node = Node(name, self, size)
        self.children[name] = new_node
    
    def get_path(self):
        if self.parent:
            return f"{self.parent.get_path()}/{self.name}"
        else:
            return "/"

    def compute_children_size(self):
        if len(self.children) > 0:
            total_size = 0
            for child in self.children.values():
                child:Node
                total_size += child.compute_children_size()
            self.computed_size = total_size
            return self.computed_size
        else:
            self.computed_size = self.size
            return self.size


    def __repr__(self) -> str:
        return f"{self.name} | {self.size}, {self.computed_size}"

    def __eq__(self, other: object) -> bool:
        if other is Node:
            return self.computed_size==other.computed_size

    def __lt__(self, other: object) -> bool:
        if other is Node:
            return self.computed_size<other.computed_size

def part1():
    root = Node("/", None)
    current = root
    for line in lines[1:]:
        line_split:list[str] = line.split()

        if line[0] == "$":
            if line_split[1]=="cd":
                match line_split[2]:
                    case "..":
                        current = current.parent
                    case _:
                        current = current.children[line_split[2]]
        elif line_split[0].isnumeric():
            current.add_child(line_split[1], int(line_split[0]))
        elif line_split[0]=="dir":
            current.add_child(line_split[1])
    root.compute_children_size()
    print(Node.directories)
        
    print(sum([dir.computed_size for dir in Node.directories if dir.computed_size<=100000]))

def part2():
    root = Node("/", None)
    current = root
    for line in lines[1:]:
        line_split:list[str] = line.split()

        if line[0] == "$":
            if line_split[1]=="cd":
                match line_split[2]:
                    case "..":
                        current = current.parent
                    case _:
                        current = current.children[line_split[2]]
        elif line_split[0].isnumeric():
            current.add_child(line_split[1], int(line_split[0]))
        elif line_split[0]=="dir":
            current.add_child(line_split[1])
    root.compute_children_size()

    unused_space = 70000000-root.computed_size

    need_to_free = 30000000-unused_space
    
    possible_deletion = [dir.computed_size for dir in Node.directories if dir.computed_size>=need_to_free]

    print(possible_deletion[-1])

part2()

