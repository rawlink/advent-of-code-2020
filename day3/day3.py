#!/usr/bin/env python3
from math import prod

TREE='#'
VECTORS = [
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2),
]

def load(file):
    with open(file) as f:
        return [line.strip() for line in f.readlines()]

def travel(map, vector):
    width = len(map[0])
    height = len(map)

    x = 0
    y = 0
    x_step, y_step = vector
    collisions = 0

    while y < height:
        if map[y][x] == TREE:
            collisions += 1
        x += x_step
        y += y_step
        x %= width
    
    return collisions

def part1(map):
    '''
    >>> part1(load('test1.txt'))
    7
    '''
    return travel(map, (3,1))

def part2(map):
    '''
    >>> part2(load('test1.txt'))
    336
    '''
    return prod(travel(map, vector) for vector in VECTORS)

def main():
    map = load('input.txt')
    value = part1(map)
    print(f'Part 1: {value}')
    assert value == 209

    value = part2(map)
    print(f'Part 1: {value}')
    assert value == 1574890240

if __name__ == '__main__':
    main()
