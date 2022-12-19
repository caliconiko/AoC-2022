import bpy
import numpy as np
import os
from numpy import ndarray
from collections import defaultdict

def get_file_path(file_name):
    return os.path.join(os.path.dirname(__file__), "..", file_name)

def read_file_lines(file_name):
    with open(get_file_path(file_name), "r") as f:
        raw = f.read()
        lines = raw.splitlines()
        return lines


lines = read_file_lines("day18.txt")

def get_man(pos1:ndarray, pos2:ndarray):
    return np.sum(np.abs(pos2-pos1))

def trigger_update():
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.object.mode_set(mode="OBJECT")
    
def add_attribute(obj_name, attr_name, type="FLOAT", domain="POINT"):
    attr = bpy.data.meshes[obj_name].attributes.new(attr_name, type, domain)
    return attr

obj = bpy.context.active_object

if obj.name != "Thing":
    raise Exception("not the thing")

geo_nodes = obj.modifiers.new("make_vertices", "NODES")
geo_nodes.node_group = bpy.data.node_groups["make_vertices"]

geo_nodes["Input_2"] = len(lines)

trigger_update()

bpy.ops.object.modifier_apply(modifier=geo_nodes.name)


positions = [int(value) for line in lines for value in line.split(",")]

pos_attr = add_attribute(obj.name, "Cube Position", "FLOAT_VECTOR", "POINT")
pos_attr.data.foreach_set("vector", positions)

values = ["a"]

attr = add_attribute(obj.name, "Test", "STRING", "POINT")
attr.data.values()[0]="a"
attr.data.update()
