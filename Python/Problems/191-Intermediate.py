#!/usr/bin/env python

import sys
import random
import heapq as hq

def main():
    size = int(sys.argv[1])
    start = divmod(int(sys.argv[2]), size)
    end = divmod(size, int(sys.argv[3]))
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
    new_galaxy = process_gravity_well(new_galaxy)
    return new_galaxy

def process_gravity_well(galaxy):
    dirs = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    print(galaxy)
    for line in galaxy:
        for space in line:
            if "G" in space:
                fy, fx = line, space
                for d in dirs:
                    x, y = d
                    x += fx
                    y += fy
                    if x < 0 or x >= len(galaxy[0]) or y < 0 or y >= len(galaxy[0]):
                        continue
                    print(str(d))
                    print(str(space))
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
    moves = []
    for d in dirs:
        x, y = from_space
        dx, dy = d
        x += dx
        y += dy
        if x < 0 or x >= len(galaxy[0]) or y < 0 or y >= len(galaxy[0]):
            continue
        if is_free(galaxy, x, y):
            moves.append((x, y))
        else:
            continue
    return moves

def is_free(galaxy, fx, fy):
    if fx < 0 or fx >= len(galaxy[0]) or fy < 0 or fy >= len(galaxy[0]):
        return False
    print(str(fx), str(fy))
    if galaxy[fy][fx] == "A":
        return False
    if galaxy[fy][fx] == "W":
        return False
    return True

if __name__ == "__main__":
    main()
