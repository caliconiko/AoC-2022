import numpy as np
import cv2

with open("day14.txt") as f:
    raw = f.read()
    lines = raw.splitlines()

def print_friendlify(arr: np.ndarray):
    return np.rot90(np.flip(arr, 1))

def print_friendlily(arr:np.ndarray):
    friendlified = print_friendlify
    print(friendlified)
    return friendlified

def print_nicely(arr:np.ndarray):
    friendlified = print_friendlify(arr)
    for line in friendlified:
        for num in line:
            character = ""
            match num:
                case 0:
                    character = "."
                case 1:
                    character = "#"
                case 2:
                    character = "O"
            print(character, end="")
        print()

def show_the_fuckin_thing(arr:np.ndarray, winname="the fukin thing"):
    friendlified = print_friendlify(arr)
    print(friendlified)
    resized = cv2.resize(friendlified,(0,0), fx=5, fy=5, interpolation=cv2.INTER_NEAREST)
    cv2.imshow(winname, resized)
    cv2.waitKey(0)

def check_position_within_area(position:np.ndarray, size_of_area:np.ndarray):
    return not (np.any(position<np.array([0,0])) or np.any(position>=size_of_area))

def part1():
    paths = [np.array([[int(point_value) for point_value in point_raw.strip().split(",")] for point_raw in line.split("->")]) for line in lines]

    THE_FUCKING_SAND_POINT = np.array([500,0])

    points = np.concatenate([np.concatenate(paths), np.array([THE_FUCKING_SAND_POINT])])
    
    print(points)

    min_world_point=np.array([np.min(points[:,0]),np.min(points[:,1])])
    max_world_point=np.array([np.max(points[:,0]),np.max(points[:,1])])

    ONE=np.array([1,1])
    ZERO=np.array([0,0])
    DOWN=np.array([0,1])
    DOWN_LEFT=np.array([-1,1])
    DOWN_RIGHT=np.array([1,1])

    world_size = max_world_point-min_world_point+ONE
    world=np.zeros(world_size)

    for path in paths:
        for i, _ in enumerate(path[:-1]):
            world:np.ndarray
            first_point = path[i]-min_world_point
            second_point = path[i+1]-min_world_point

            line_points=np.array([first_point,second_point])

            min_point=np.array([np.min(line_points[:,0]),np.min(line_points[:,1])])
            max_point=np.array([np.max(line_points[:,0]),np.max(line_points[:,1])])
            world[min_point[0]:max_point[0]+1, min_point[1]:max_point[1]+1]=1

    sands = 0
    while True:
        sand_position = THE_FUCKING_SAND_POINT-min_world_point

        sand_within_world = check_position_within_area(sand_position, world_size)
        while sand_within_world:
            sand_down = sand_position+DOWN
            sand_down_left = sand_position+DOWN_LEFT
            sand_down_right = sand_position+DOWN_RIGHT

            potestial_sand_positions = [sand_down, sand_down_left, sand_down_right]

            settled = False

            for i, potential_sand_position in enumerate(potestial_sand_positions):
                if check_position_within_area(potential_sand_position, world_size):
                    if world[*potential_sand_position]<1:
                        sand_position=potential_sand_position
                        break
                    elif i+1>=len(potestial_sand_positions):
                        settled=True
                else:
                    sand_position=potential_sand_position
                    settled=True

            sand_within_world = check_position_within_area(sand_position, world_size)

            if settled:
                break

        if sand_within_world:
            world[*sand_position]=2
            sands+=1
        else:
            break
    print_nicely(world)
    print(min_world_point)
    print(sands)

def part2():
    paths = [np.array([[int(point_value) for point_value in point_raw.strip().split(",")] for point_raw in line.split("->")]) for line in lines]

    THE_FUCKING_SAND_POINT = np.array([500,0])

    points = np.concatenate([np.concatenate(paths), np.array([THE_FUCKING_SAND_POINT])])
    
    print(points)

    x_offset_min = (np.max(points[:,1])+3)

    min_world_point=np.array([THE_FUCKING_SAND_POINT[0]-x_offset_min,np.min(points[:,1])])
    max_world_point=np.array([THE_FUCKING_SAND_POINT[0]+x_offset_min,np.max(points[:,1])+1])

    ONE=np.array([1,1])
    UP=np.array([0,-1])
    LEFT=np.array([-1,0])
    RIGHT=np.array([1,0])
    

    world_size = max_world_point-min_world_point+ONE
    world=np.zeros(world_size)

    for path in paths:
        for i, _ in enumerate(path[:-1]):
            world:np.ndarray
            first_point = path[i]-min_world_point
            second_point = path[i+1]-min_world_point

            line_points=np.array([first_point,second_point])

            min_point=np.array([np.min(line_points[:,0]),np.min(line_points[:,1])])
            max_point=np.array([np.max(line_points[:,0]),np.max(line_points[:,1])])
            world[min_point[0]:max_point[0]+1, min_point[1]:max_point[1]+1]=1

    sand_mask = np.zeros_like(world)

    sand_mask[*(THE_FUCKING_SAND_POINT-min_world_point)]=1
    
    for y in range(1,sand_mask.shape[1]):
        for x in range(sand_mask.shape[0]):
            current_position = np.array([x,y])
            upper = sand_mask[*(current_position+UP)]>0
            lefter = False
            if check_position_within_area(current_position+UP+LEFT, sand_mask.shape):
                lefter = sand_mask[*(current_position+UP+LEFT)]>0
            righter = False
            if check_position_within_area(current_position+UP+RIGHT, sand_mask.shape):
                righter = sand_mask[*(current_position+UP+RIGHT)]>0


            if lefter or upper or righter:
                sand_mask[x,y]=1

    air_mask = world.copy()

    for y in range(1,air_mask.shape[1]):
        for x in range(air_mask.shape[0]):
            current_position = np.array([x,y])
            upper = air_mask[*(current_position+UP)]>0
            lefter = False
            if check_position_within_area(current_position+UP+LEFT, air_mask.shape):
                lefter = air_mask[*(current_position+UP+LEFT)]>0
            righter = False
            if check_position_within_area(current_position+UP+RIGHT, air_mask.shape):
                righter = air_mask[*(current_position+UP+RIGHT)]>0


            if lefter and upper and righter:
                air_mask[x,y]=1

    actual_mask = cv2.bitwise_xor(sand_mask, air_mask)
    show_the_fuckin_thing(actual_mask)
    show_the_fuckin_thing(sand_mask, "ALLLL THE SAND")
    show_the_fuckin_thing(air_mask, "NO SAND ALLOWED >:(")

    print(np.sum(actual_mask))

part2()