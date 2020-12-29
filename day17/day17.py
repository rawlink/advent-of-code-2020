#!/usr/bin/env python3
from itertools import product

ITERATIONS = 6

NEIGHBORS = set(product([-1, 0, 1], repeat=3))
NEIGHBORS.remove((0,0,0))

FOURD_NEIGHBORS = set(product([-1, 0, 1], repeat=4))
FOURD_NEIGHBORS.remove((0,0,0,0))

def load(file):
    with open(file) as f:
        lines = [line.strip() for line in f.readlines()]
    
    # Store the cubes in a set so we can store them sparsely.
    cubes = set()
    for y,line in enumerate(lines):
        for x,cube in enumerate(line):
            if cube == '#':
                cubes.add((x,y,0, 0))

    # A bounding box around the seed with a buffer of 1 empty box all the way around. We want to check all empty neighbors.
    limits = ((-1, -1, -1, -1), (len(lines[0]), len(lines), 1, 1))

    return cubes, limits

def neighbors(cube, cubes):
    x,y,z = cube
    total = 0
    for neighbor in NEIGHBORS:
        dx, dy, dz = neighbor
        if (x + dx, y + dy, z + dz) in cubes:
            total += 1

    return total

def part1(cubes, limits, iterations):
    '''
    >>> part1(*load('test1.txt'), ITERATIONS)
    112
    '''
    x_min = limits[0][0]
    x_max = limits[1][0]
    y_min = limits[0][1]
    y_max = limits[1][1]
    z_min = limits[0][2]
    z_max = limits[1][2]

    cubes = [(x,y,z) for x,y,z,_ in cubes]

    prev = set()
    curr = cubes

    for i in range(iterations): 
        prev = curr
        curr = set()
        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                for z in range(z_min, z_max + 1):
                    cube = (x, y, z)
                    if (cube in prev and 2 <= neighbors(cube, prev) <= 3) or (cube not in prev and neighbors(cube, prev) == 3):
                        curr.add(cube)
                        if x == x_min:
                            x_min -= 1
                        if x == x_max:
                            x_max += 1
                        if y == y_min:
                            y_min -= 1
                        if y == y_max:
                            y_max += 1
                        if z == z_min:
                            z_min -= 1
                        if z == z_max:
                            z_max += 1

    return len(curr)

def fourd_neighbors(cube, cubes):
    x,y,z,w = cube
    total = 0
    for neighbor in FOURD_NEIGHBORS:
        dx, dy, dz, dw = neighbor
        if (x + dx, y + dy, z + dz, w + dw) in cubes:
            total += 1

    return total

def part2(cubes, limits, iterations):
    '''
    >>> part2(*load('test1.txt'), ITERATIONS)
    848
    '''
    x_min = limits[0][0]
    x_max = limits[1][0]
    y_min = limits[0][1]
    y_max = limits[1][1]
    z_min = limits[0][2]
    z_max = limits[1][2]
    w_min = limits[0][3]
    w_max = limits[1][3]

    prev = set()
    curr = cubes

    for i in range(iterations): 
        prev = curr
        curr = set()
        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                for z in range(z_min, z_max + 1):
                    for w in range(w_min, w_max + 1):
                        cube = (x, y, z, w)
                        if (cube in prev and 2 <= fourd_neighbors(cube, prev) <= 3) or (cube not in prev and fourd_neighbors(cube, prev) == 3):
                            curr.add(cube)
                            if x == x_min:
                                x_min -= 1
                            if x == x_max:
                                x_max += 1
                            if y == y_min:
                                y_min -= 1
                            if y == y_max:
                                y_max += 1
                            if z == z_min:
                                z_min -= 1
                            if z == z_max:
                                z_max += 1
                            if w == w_min:
                                w_min -= 1
                            if w == w_max:
                                w_max += 1

    return len(curr)
    

def main():
    # I'm sure this can be sped up with prior layer precalculation similar to the conway-like seat problem for day11, but
    # the answers come quickly enough without the optimization.
    cubes, limits = load('input.txt')
    value = part1(cubes, limits, ITERATIONS)
    print(f'Part 1: {value}')
    assert value == 395

    value = part2(cubes, limits, ITERATIONS)
    print(f'Part 2: {value}')
    assert value == 2296

if __name__ == '__main__':
    main()