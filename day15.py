import numpy as np
from numpy import ndarray
from collections import defaultdict


with open("day15.txt") as f:
    raw = f.read()
    lines = raw.splitlines()

def get_man(pos1:ndarray, pos2:ndarray):
    return np.sum(np.abs(pos2-pos1))

def part1():

    sensors = np.array(
        [
            [
                int(value_raw[2:]) for value_raw in line.replace(",", "").replace(":", "").split()[2:4]
            ]
         for line in lines
        ]
    )

    closest_beacons = np.array(
        [
            [
                int(value_raw[2:]) for value_raw in line.replace(",", "").replace(":", "").split()[8:]
            ]
         for line in lines
        ]
    )

    target_y =2000000
    number_of_sensors = sensors.shape[0]

    intersections = defaultdict(list)

    for i in range(number_of_sensors):
        sensor_pos = sensors[i]
        beacon_pos = closest_beacons[i]

        man_distance = get_man(sensor_pos, beacon_pos)
        y_distance = abs(target_y-sensor_pos[1])
        if y_distance<=man_distance:
            x_distance = man_distance-y_distance

            intersect_x_min = sensor_pos[0]-x_distance
            intersect_x_max = sensor_pos[0]+x_distance

            intersections[intersect_x_min].append(1)
            intersections[intersect_x_max].append(-1)

    intersections_keys = sorted(intersections.keys())
    print(intersections_keys)
    intersection_sum = 0
    target_sum = 0
    for keyi, key in enumerate(intersections_keys[:-1]):
        intersection_sum+=sum(intersections[key])
        if intersection_sum>0:
            target_sum+=intersections_keys[keyi+1]-key
    print(target_sum)
    print([intersections[key] for key in intersections_keys])
    
part1()