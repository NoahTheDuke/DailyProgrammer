#!/usr/bin/env python

import sys
import random
import heapq as hq

def main():
    size = int(sys.argv[1])
    start = (int(sys.argv[2]), int(sys.argv[3]))
    end = (int(sys.argv[4]), int(sys.argv[5]))
    print("Size of the galazy: {}".format(size))
    print("Start: {}, End: {}".format(start, end))
    galaxy = generate(size, start, end)
    for row in print_galaxy(galaxy):
        print(row)
    result = pathfind(galaxy, start, end)
    if result:
        print(str(result))

def print_galaxy(galaxy):
    place = []
    for lines in galaxy:
        place.append(" ".join(lines))
    return place

def generate(size, start, end):
    fullsize = size * size
    asteroids = int(fullsize * 0.20)
    gravity_wells = int(fullsize * 0.05)
    empty_space = fullsize - asteroids - gravity_wells
    galaxy = ["A"] * asteroids + ["G"] * gravity_wells + ["."] * empty_space
    random.shuffle(galaxy)
    new_galaxy = []
    for el in range(size):
        galaxy_line = []
        for le in range(size):
            galaxy_line.append(galaxy.pop())
        new_galaxy.append(galaxy_line)
    return process_gravity_well(place_start_end_points(new_galaxy, start, end))

def place_start_end_points(galaxy, start, end):
    fx, fy = start
    tx, ty = end
    galaxy[fy][fx] = "S"
    galaxy[ty][tx] = "E"
    return galaxy

def process_gravity_well(galaxy):
    dirs = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
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
        print("current: {}".format(current))
        if current == end:
            break
        for potential in neighbors(galaxy, current):
            print("potential: {}".format(potential))
            if potential not in came_from:
                priority = heuristic(end, potential)
                hq.heappush(frontier, priority)
                came_from[potential] = current

def heuristic(a, b):
    # Manhattan distance on a square grid
    return abs(a[1] - b[1]) + abs(a[0] - b[0])

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
        if galaxy[y][x] == "A":
            continue
        if galaxy[y][x] == "W":
            continue
        else:
            neighbor.append((x, y))
    return neighbor


if __name__ == "__main__":
    main()
