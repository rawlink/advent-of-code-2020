#!/usr/bin/env python3
TREE='#'
VECTORS = [
    [1,1],
    [3,1],
    [5,1],
    [7,1],
    [1,2],
]

def main(input):
    with open(input) as f:
        lines = [line.strip() for line in f.readlines()]

    width = len(lines[0])
    height = len(lines)

    product = 1
    for vector in VECTORS:
        x = 0
        y = 0
        x_step = vector[0]
        y_step = vector[1]
        collisions = 0

        while y < height:
            if lines[y][x] == TREE:
                collisions += 1

            x += x_step
            y += y_step

            x %= width
        print(f'COLLISIONS {vector}: {collisions}')
        product *= collisions

    print(f'PRODUCT: {product}')

if __name__ == '__main__':
    main('map.txt')
