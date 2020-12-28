#!/usr/bin/env python3
from copy import deepcopy

FLOOR = -1
EMPTY = 0
OCCUPIED = 1

CHAR_FLOOR = '.'
CHAR_SEAT = 'L'

VECTORS = [
    (-1, 0),
    (-1, 1),
    (0,1),
    (1,1),
    (1,0),
    (1,-1),
    (0,-1),
    (-1,-1)
]
def map_type(c):
    if c == CHAR_FLOOR:
        return FLOOR
    elif c == CHAR_SEAT:
        return EMPTY

    raise Exception('Unknown type')

def load(file):
    with open(file) as f:
        seating = [list(map(map_type,line.strip())) for line in f.readlines()]

    return seating

def immediate_neighbor(seating, row, seat, value, vector):
    row += vector[0]
    seat += vector[1]

    if row < 0 or row >= len(seating):
        return False

    if seat < 0 or seat >= len(seating[row]):
        return False

    return seating[row][seat] == value

def line_of_sight_neighbor(seating, row, seat, value, vector):
    while True:
        row += vector[0]
        seat += vector[1]

        if row < 0 or row >= len(seating):
            return False

        if seat < 0 or seat >= len(seating[row]):
            return False
        
        if seating[row][seat] == FLOOR:
            continue

        return seating[row][seat] == value

def count_neighbors(seating, row, seat, value, rule):
    if seating[row][seat] == FLOOR:
        raise Exception('Cowardly refusing to count neighbors of floor')

    count = 0
    for vector in VECTORS:
        if rule(seating, row, seat, value, vector):
            count += 1

    return count

def count_seating(seating, value):
    return sum([row.count(value) for row in seating])

def part1_seating_rule(src):
    dst = deepcopy(src)

    for row in range(len(src)):
        for seat in range(len(src[row])):
            if src[row][seat] == EMPTY and count_neighbors(src, row, seat, OCCUPIED, immediate_neighbor) == 0:
                dst[row][seat] = OCCUPIED
            if src[row][seat] == OCCUPIED and count_neighbors(src, row, seat, OCCUPIED, immediate_neighbor) >= 4:
                dst[row][seat] = EMPTY

    return dst

def part2_seating_rule(src):
    dst = deepcopy(src)

    for row in range(len(src)):
        for seat in range(len(src[row])):
            if src[row][seat] == EMPTY and count_neighbors(src, row, seat, OCCUPIED, line_of_sight_neighbor) == 0:
                dst[row][seat] = OCCUPIED
            if src[row][seat] == OCCUPIED and count_neighbors(src, row, seat, OCCUPIED, line_of_sight_neighbor) >= 5:
                dst[row][seat] = EMPTY

    return dst

def iterate(seating, rule):
    '''
    >>> iterate(load('test1.txt'), part1_seating_rule)
    37
    >>> iterate(load('test1.txt'), part2_seating_rule)
    26
    '''
    last = None
    current = seating

    while current != last:
        last = current
        current = rule(last)

    return count_seating(current, OCCUPIED)

def main():
    seating = load('input.txt')
    value = iterate(seating, part1_seating_rule)
    print(f'Part 1: {value}')
    assert value == 2448

    value = iterate(seating, part2_seating_rule)
    print(f'Part 2: {value}')
    assert value == 2234

if __name__ == '__main__':
    main()