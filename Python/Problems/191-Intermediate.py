#!/usr/bin/env python

import sys
import random
import heapq as hq

def main():
    size = int(sys.argv[1])
    start = int(sys.argv[2])
    end = int(sys.argv[3])
    print("Size of the galazy: {}".format(size))
    print("Start: {}, End: {}".format(start, end))
    galaxy = generate(size, start, end)
    for row in print_galaxy(galaxy):
        print(row)
    result = pathfind(galaxy, start, end)
    if result:
        print(str(result))
        print("Found a path!")

def print_galaxy(galaxy):
    place = []
    for lines in galaxy:
        place.append(" ".join(lines))
    return place

def num_to_char(num):
    if num < 31:
        return "A"
    elif num < 41:
        return "G"
    else:
        return "."

def generate(size, start, end):
    fullsize = size * size
    galaxy = [num_to_char(x) for x in [random.randrange(1,101) for _ in range(fullsize)]]
    new_galaxy = []
    for el in range(size):
        new__galaxy = []
        for le in range(size):
            new__galaxy.append(galaxy.pop())
        new_galaxy.append(new__galaxy)
    return process_gravity_well(new_galaxy)

def process_gravity_well(galaxy):
    dirs = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    print(galaxy)
    for lx, line in enumerate(galaxy):
        for sx, space in enumerate(line):
            if "G" in space:
                fy, fx = lx, sx
                for d in dirs:
                    x, y = d
                    x += fx
                    y += fy
                    if x < 0 or x >= len(galaxy[0]) or y < 0 or y >= len(galaxy[0]):
                        continue
                    if galaxy[y][x] == ".":
                        galaxy[y][x] = "W"
    return galaxy

def pathfind(galaxy, start, end):
    frontier = []
    hq.heappush(frontier, start)
    came_from = {}
    came_from[start] = None

    while frontier:
        current = hq.heappop(frontier)
        for potential in neighbors(galaxy, current):
            if potential not in came_from:
                hq.heappush(frontier, potential)
                came_from[potential] = current
    return came_from

def neighbors(galaxy, from_space):
    dirs = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    neighbor = []
    for d in dirs:
        x, y = from_space
        dx, dy = d
        x += dx
        y += dy
        if x < 0 or x >= len(galaxy[0]) or y < 0 or y >= len(galaxy[0]):
            continue
        if galaxy[fy][fx] == "A":
            continue
        if galaxy[fy][fx] == "W":
            continue
        else:
            neighbor.append((x, y))
    return neighbor


if __name__ == "__main__":
    main()
