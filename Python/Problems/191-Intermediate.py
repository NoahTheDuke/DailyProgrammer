#!/usr/bin/env python

import sys
import random

def main():
    size = int(sys.argv[1])
    print(size)
    galaxy = generate(size)
    print(galaxy)
    with open("191-Galaxy.txt", "w") as text_file:
        print(galaxy, file=text_file)

def generate(size):
    fullsize = size * size
    edge = ' ' * size + ' \n'
    galaxy = edge + '\n'.join(' ' + y for y in list(map(''.join, zip(*[iter([num_to_char(x) for x in [random.randrange(1,101) for _ in range(fullsize)]])] * size)))) + edge + edge
    return galaxy

def num_to_char(num):
    if num < 31:
        return "A"
    elif num < 41:
        return "G"
    else:
        return "."

if __name__ == "__main__":
    main()
