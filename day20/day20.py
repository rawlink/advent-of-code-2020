#!/usr/bin/env python3
import re
import math

INPUT_ON = '#'
PIXEL_OFF = 0
PIXEL_ON = 1
PIXEL_BIO = 2



EDGE_TOP = 0
EDGE_RIGHT = 1
EDGE_BOTTOM = 2
EDGE_LEFT = 3

# ______________________
# |                  # |
# |#    ##    ##    ###|
# | #  #  #  #  #  #   |
# ^^^^^^^^^^^^^^^^^^^^^^
SEA_MONSTER = [
    (18, 0),
    (0, 1), (5, 1), (6, 1), (11, 1), (12, 1), (17, 1), (18, 1), (19, 1),
    (1, 2), (4, 2), (7, 2), (10, 2), (13, 2), (16, 2)
]
SEA_MONSTER_MAX_X = 19
SEA_MONSTER_MAX_Y = 2


def load(file):
    with open(file) as f:
        raw_tiles = [tile.splitlines() for tile in f.read().split('\n\n')]

    tiles = {}
    pattern = re.compile('^Tile (\d+):$')
    for tile in raw_tiles:
        if len(tile) <= 0:
            continue
        match = pattern.match(tile[0].strip())
        id = int(match.group(1))
        tiles[id] = [[PIXEL_ON if c == INPUT_ON else PIXEL_OFF for c in list(row)] for row in tile[1:]]

    return tiles


def rotate(tile, rotations):
    if not 0 <= rotations < 4:
        raise Exception(f'Bad multiple of ninety (0-3): {rotations}')
    if rotations == 1:
        tile = list(zip(*tile[::-1]))
        return [list(row) for row in tile]
    elif rotations == 2:
        return [list(reversed(row)) for row in tile[::-1]]
    elif rotations == 3:
        tile = list(zip(*tile))[::-1]
        return [list(row) for row in tile]
    else:
        return tile


def get_edges(tile):
    edges = []
    edges.append(tile[0])  # EDGE_TOP
    edges.append([row[-1] for row in tile])  # EDGE_RIGHT
    edges.append(tile[-1])  # EDGE_BOTTOM
    edges.append([row[0] for row in tile])  # EDGE_LEFT

    return edges

def get_adjacencies(tiles):
    edge_map = {}
    adjacencies = {}
    for id, tile in tiles.items():
        edges = get_edges(tile)
        for idx, edge in enumerate(edges):
            edge_id = ''.join(map(lambda e: str(e), edge))
            if edge_id not in edge_map:
                edge_map[edge_id] = (id, idx)  # id, edge
                edge_id = edge_id[::-1]
                edge_map[edge_id] = (id, idx)  # id, edge
            else:
                match_tile, match_edge = edge_map[edge_id]
                adjacencies[(id, idx)] = (match_tile, match_edge)
                adjacencies[(match_tile, match_edge)] = (id, idx)

    return adjacencies


def get_corners(adjacencies):
    edge_counts = {}
    for (id, _) in adjacencies.keys():
        if id in edge_counts:
            edge_counts[id] += 1
            if edge_counts[id] > 4:
                raise Exception('Oh My!')
        else:
            edge_counts[id] = 1

    corners = [id for (id, count) in edge_counts.items() if count == 2]

    return corners


def calc_rotation(pos, target):
    return (target - pos) % 4


def clockwise_edges_for_corner(tile_id, adjacencies):
    max_edge = 0
    min_edge = 3
    for i in range(4):
        if (tile_id, i) in adjacencies:
            min_edge = min(min_edge, i)
            max_edge = max(max_edge, i)

    if min_edge == 0 and max_edge == 3:
        min_edge, max_edge = max_edge, min_edge

    return min_edge, max_edge


def strip_tile(tile):
    return [[col for col in row[1:-1]] for row in tile[1:-1]]


def flip_tile_v(tile):
    return tile[::-1]


def flip_tile_h(tile):
    return [row[::-1] for row in tile]


def opposite_edge(edge):
    return (edge + 2) % 4

def create_image(tiles):
    tiles_width = len(tiles[0])
    tiles_height = len(tiles)
    a_tile = tiles[0][0]
    tile_width = len(a_tile[0])
    tile_height = len(a_tile)

    width = tiles_width * tile_width
    height = tiles_height * tile_height
    
    image = [[0] * width for row in range(height)]

    for tiles_row_idx, tiles_row in enumerate(tiles):
        tile_base_y = tiles_row_idx * tile_height
        for tiles_col_idx, tile in enumerate(tiles_row):
            tile_base_x = tiles_col_idx * tile_width
            for pixel_row_idx, tile_row in enumerate(tile):
                y = tile_base_y + pixel_row_idx
                for pixel_col_idx, pixel in enumerate(tile_row):
                    x = tile_base_x + pixel_col_idx
                    image[y][x] = pixel

    return image

def mark_seamonsters(image):
    total = 0
    for y, row in enumerate(image[:-SEA_MONSTER_MAX_Y]):
        for x in range(len(row[:-SEA_MONSTER_MAX_X])):
            found = True
            for (dx, dy) in SEA_MONSTER:
                if image[y + dy][x + dx] != PIXEL_ON:
                    found = False
            if found:
                total += 1
                for (dx, dy) in SEA_MONSTER:
                    image[y + dy][x + dx] = PIXEL_BIO

    return total

def find_and_mark_seamonsters(image):
    for i in range(8):
        if i == 4:
            image = flip_tile_v(image)
        if mark_seamonsters(image) > 0:
            return image
        image = rotate(image, 1)

    raise Exception('No monsters found :-/')

def calc_roughness(image):
    return sum(i for row in image for i in row if i == 1)

def rotate_around_edge(edge, rotation):
    return (edge + rotation) % 4

def part1(tiles):
    '''
    >>> part1(load('test1.txt'))
    20899048083289
    '''
    adjacencies = get_adjacencies(tiles)
    return math.prod(get_corners(adjacencies))

def part2(tiles):
    '''
    >>> part2(load('test1.txt'))
    273
    '''
    adjacencies = get_adjacencies(tiles)
    corners = get_corners(adjacencies)

    # Figure out how we want to rotate an arbitrary corner to be our first piece in the "upper-left" corner. The 2 linked
    # edges need to be on the bottom and the right. We need to rotate the clockwise most edge into position 2

    # EDGE POSITIONS
    #   0
    # 3   1
    #   2
    curr_tile = corners[0]
    left_tile = curr_tile
    right_edge, bottom_edge = clockwise_edges_for_corner(curr_tile, adjacencies)
    stripped_tile = strip_tile(tiles[curr_tile])
    rotations = calc_rotation(bottom_edge, EDGE_BOTTOM)
    rotated_tile = rotate(stripped_tile, rotations)
    row = 0
    connected_tiles = [[rotated_tile]]

    tile_in_row = 0
    curr_tiles = [curr_tile]
    previous_tiles = []
    while True:
        if (curr_tile, right_edge) in adjacencies:
            tile_in_row += 1
            (curr_tile, left_edge) = adjacencies[(curr_tile, right_edge)]
            stripped_tile = strip_tile(tiles[curr_tile])
            rotations = calc_rotation(left_edge, EDGE_LEFT)
            rotated_tile = rotate(stripped_tile, rotations)
            if row == 0:
                flip = (curr_tile, rotate_around_edge(left_edge, 1)) in adjacencies
            else:
                if (curr_tile, rotate_around_edge(left_edge, 1)) not in adjacencies:
                    flip = True
                else:
                    flip = adjacencies[(curr_tile, rotate_around_edge(left_edge, 1))][0] != previous_tiles[tile_in_row]
            if flip:
                rotated_tile = flip_tile_v(rotated_tile)
            right_edge = opposite_edge(left_edge)
            curr_tiles.append(curr_tile)
            connected_tiles[row].append(rotated_tile)
        else:
            if (left_tile, bottom_edge) not in adjacencies:
                break
            tile_in_row = 0
            row += 1
            (curr_tile, top_edge) = adjacencies[(left_tile, bottom_edge)]
            assert adjacencies[(curr_tile, top_edge)][0] == curr_tiles[tile_in_row]
            left_tile = curr_tile
            bottom_edge = opposite_edge(top_edge)
            stripped_tile = strip_tile(tiles[curr_tile])
            rotations = calc_rotation(top_edge, EDGE_TOP)
            rotated_tile = rotate(stripped_tile, rotations)
            right_edge = rotate_around_edge(top_edge, 1)
            if (curr_tile, right_edge) not in adjacencies:
                rotated_tile = flip_tile_h(rotated_tile)
                right_edge = opposite_edge(right_edge)
            previous_tiles = curr_tiles
            curr_tiles = [curr_tile]
            connected_tiles.append([rotated_tile])

    image = create_image(connected_tiles)

    image = find_and_mark_seamonsters(image)

    return calc_roughness(image)

def print_image(image):
    print('========================================================================================================================================================')
    for row in image:
        print(row)
    print('========================================================================================================================================================')

# This will only work for completely uniquely edged tiles and distinct sea monster signatures (although the sea monster
# thing would be an easy fix). Also, this one isn't going to win any code golf contests :-P
# Essentially build an adjacency list of all the pieces, and then take one corner and build it out into a grid, row by row.
def main():
    tiles = load('input.txt')
    value = part1(tiles)
    print(f'Part 1: {value}')
    assert value == 64802175715999

    value = part2(tiles)
    print(f'Part 2: {value}')
    assert value == 2146

if __name__ == '__main__':
    main()