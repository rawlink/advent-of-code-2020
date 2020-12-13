#!/usr/bin/env python3

RIGHT = 'R'
LEFT = 'L'
FORWARD = 'F'

NORTH = 'N'
EAST = 'E'
SOUTH = 'S'
WEST = 'W'

DIRECTIONS = {
    'N': (1, 0),
    'E': (0, 1),
    'S': (-1, 0),
    'W': (0, -1)
}

COMPASS = {
    0: 'N',
    90: 'E',
    180: 'S',
    270: 'W'
}

def parse(step):
    return (step[0], int(step[1:]))

def load(file):
    with open(file) as f:
        step = [parse(line.strip()) for line in f.readlines()]
    return step

def rotate(rotation, instruction, value):
    if instruction != LEFT and instruction != RIGHT:
        raise Exception(f'Unknown rotation: {rotation}')

    direction = 0
    if instruction == LEFT:
        direction = -1
    elif instruction == RIGHT:
        direction = 1

    rotation += direction * value

    while rotation < 0:
        rotation += 360

    while rotation >= 360:
        rotation -= 360

    return rotation

def part1(route):
    x = 0
    y = 0
    ship_rotation = 90

    for step in route:
        instruction = step[0]
        value = step[1]

        if instruction == RIGHT or instruction == LEFT:
            ship_rotation = rotate(ship_rotation, instruction, value)
        else:
            direction = DIRECTIONS[COMPASS[ship_rotation]]
            if instruction != FORWARD:
                direction = DIRECTIONS[instruction]
            x += direction[0] * value
            y += direction[1] * value
    
    return abs(x) + abs(y)


def main():
    route = load('test1.txt')
    manhattan = part1(route)
    print(f'Test 1 - Manhattan: {manhattan}')
    assert manhattan == 25

    route = load('input.txt')
    manhattan = part1(route)
    print(f'Manhattan: {manhattan}')

if __name__ == '__main__':
    main()