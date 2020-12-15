#!/usr/bin/env python3

RIGHT = 'R'
LEFT = 'L'
FORWARD = 'F'

NORTH = 'N'
EAST = 'E'
SOUTH = 'S'
WEST = 'W'

DIRECTIONS = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0)
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
        raise Exception(f'Unknown rotation instruction: {instruction}')

    if value % 90 != 0:
        raise Exception(f'Invalid rotation ({value}). Rotations must be increments of 90.')

    direction = 0

    if instruction == LEFT:
        direction = -1
    else:
        direction = 1

    rotation += direction * value

    rotation %= 360

    return rotation

def rotate_wp(x, y, instruction, value):
    if instruction != LEFT and instruction != RIGHT:
        raise Exception(f'Unknown rotation instruction: {instruction}')

    if instruction == LEFT:
        instruction = RIGHT
        value = -value

    value %= 360

    if value == 0:
        return x, y
    elif value == 90:
        return y, -x
    elif value == 180:
        return -x, -y
    elif value == 270:
        return -y, x

    raise Exception(f'Invalid rotation ({value}). Rotations must be increments of 90.')

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

def part2(route):
    x = 0
    y = 0
    wp_x = 10
    wp_y = 1

    for step in route:
        instruction = step[0]
        value = step[1]

        if instruction == FORWARD:
            x += wp_x * value
            y += wp_y * value
        elif instruction == RIGHT or instruction == LEFT:
            (wp_x, wp_y) = rotate_wp(wp_x, wp_y, instruction, value)
        else:
            direction = DIRECTIONS[instruction]
            wp_x += direction[0] * value
            wp_y += direction[1] * value

    return abs(x) + abs(y)


def main():
    route = load('test1.txt')
    manhattan = part1(route)
    print(f'Test 1 - Part 1: {manhattan}')
    assert manhattan == 25
    manhattan = part2(route)
    print(f'Test 1 - Part 2: {manhattan}')
    assert manhattan == 286

    route = load('input.txt')
    manhattan = part1(route)
    print(f'Part 1: {manhattan}')
    manhattan = part2(route)
    print(f'Part 2: {manhattan}')

if __name__ == '__main__':
    main()