#!/usr/bin/env python

import sys
import random
import heapq as hq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        hq.heappush(self.elements, (priority, item))

    def get(self):
        return hq.heappop(self.elements)[1]

class GalaxyGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.weights = {}
        self.characters = {}
        self.walls = []

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        x, y = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1), (x+1, y+1), (x-1, y-1), (x-1, y+1), (x-1, y+1)]
        if (x + y) % 2 == 0: results.reverse()
        return filter(self.passable, filter(self.in_bounds, results))

    def cost(self, a, b):
        return self.weights.get(b, 1)

    def print_tile(self, x, y):
        tile = "."
        if (x, y) in self.characters:
            tile = self.characters.get((x, y), 1)
        return tile

    def print_grid(self):
        results = []
        for y in range(self.height):
            line = []
            for x in range(self.width):
                line.append(self.print_tile(x, y))
            results.append(" ".join(line))
        return results

def main():
    size = int(sys.argv[1])
    start = (int(sys.argv[2]), int(sys.argv[3]))
    end = (int(sys.argv[4]), int(sys.argv[5]))
    print("Size of the galazy: {}".format(size))
    print("Start: {}, End: {}".format(start, end))
    galaxy = GalaxyGrid(size, size)
    galaxy = generate(galaxy, size, start, end)
    galaxy_map = galaxy.print_grid()
    for lines in galaxy_map:
        print(str(lines))
    result = astar_pathfind(galaxy, start, end)
    if end in result:
        result_map = reconstruct_path(galaxy, result, start, end)
        galaxy_map = result_map.print_grid()
        print()
        for lines in galaxy_map:
            print(str(lines))
    else:
        print("No path found.")

def generate(graph, size, start, end):
    fullsize = size * size
    asteroids = int(fullsize * .25)
    gravity_wells = int(fullsize * 0.025)
    while asteroids > 0:
        potential = (random.randrange(0, size), random.randrange(0, size))
        if potential not in graph.characters:
            graph.characters[potential] = "A"
            graph.walls.append(potential)
            asteroids = asteroids - 1
    while gravity_wells > 0:
        potential = (random.randrange(0, size), random.randrange(0, size))
        if potential not in graph.characters:
            graph.characters[potential] = "G"
            graph.walls.append(potential)
            for wells in graph.neighbors(potential):
                graph.walls.append(wells)
            gravity_wells = gravity_wells - 1
    graph.characters[start] = "S"
    if start in graph.walls:
        graph.walls.remove(start)
    graph.characters[end] = "E"
    if end in graph.walls:
        graph.walls.remove(end)
    return graph

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

def astar_pathfind(galaxy, start, end):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == end:
            break

        for potential in galaxy.neighbors(current):
            new_cost = cost_so_far[current] + galaxy.cost(current, potential)
            if potential not in cost_so_far or new_cost < cost_so_far[potential]:
                cost_so_far[potential] = new_cost
                priority = new_cost + heuristic(end, potential)
                frontier.put(potential, priority)
                came_from[potential] = current
    return came_from#, cost_so_far

def reconstruct_path(graph, came_from, start, end):
    current = end
    path = [current]
    while current != start:
        current = came_from[current]
        graph.characters[current] = "O"
    return graph

def heuristic(f, t):
    fx, fy = f
    tx, ty = t
    return abs(fx - tx) + abs(fy - ty)


if __name__ == "__main__":
    main()
