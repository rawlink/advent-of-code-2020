#!/usr/bin/env python3

DIRECTIONS = {
    'ne': (1,1),
    'e': (2, 0),
    'se': (1, -1),
    'sw': (-1, -1),
    'w': (-2, 0),
    'nw': (-1, 1)
}

def parse_steps(steps):
    pos = 0
    steps_len = len(steps)
    parsed_steps = []
    while pos < steps_len:
        curr = steps[pos]
        if curr == 'e' or curr == 'w':
            delta = 1
        else:
            delta = 2
        parsed_steps.append(steps[pos:pos + delta])
        pos += delta
    return parsed_steps


def load(file):
    with open(file) as f:
        instructions = [parse_steps(steps.strip()) for steps in f.readlines()]
    return instructions

def part1(instructions):
    tiles = set()

    for steps in instructions:
        x = 0
        y = 0
        for step in steps:
            dx, dy = DIRECTIONS[step]
            x += dx
            y += dy
        tile = (x, y)
        if tile in tiles:
            tiles.remove(tile)
        else:
            tiles.add(tile)

    return tiles

def create_test_set(black_tiles):
    test_set = set()
    for tile in black_tiles:
        test_set.add(tile)
        x, y = tile
        for dx, dy in DIRECTIONS.values():
            test_set.add((x + dx, y + dy))

    return test_set

def count_neighbors(tile, tiles):
    count = 0
    x, y = tile
    for dx, dy in DIRECTIONS.values():
        if (x + dx, y + dy) in tiles:
            count += 1

    return count

def part2(black_tiles):
    curr = black_tiles.copy()

    for _ in range(100):
        prev = curr
        test_set = create_test_set(prev)
        curr = set()

        for tile in test_set:
            neighbors = count_neighbors(tile, prev)
            if (tile in prev and 0 < neighbors <= 2) or(tile not in prev and neighbors == 2):
                curr.add(tile)

    return len(curr)

# It took a few minutes of pencil and paper time to move from a tile class (yuck), to using a 2d array that had the alternating
# rows being at "half-step" offsets (also yuck), to finally going to a geometric solution using the coordinates of the centers
# of the tiles surrounding the current tile.
def main():
    instructions = load('test1.txt')
    black_tiles = part1(instructions)
    value = len(black_tiles)
    print(f'Test 1 - Part 1: {value}')
    assert value == 10
    value = part2(black_tiles)
    print(f'Test 1 - Part 2: {value}')
    assert value == 2208

    instructions = load('input.txt')
    black_tiles = part1(instructions)
    value = len(black_tiles)
    print(f'Part 1: {value}')
    value = part2(black_tiles)
    print(f'Part 2: {value}')

if __name__ == '__main__':
    main()