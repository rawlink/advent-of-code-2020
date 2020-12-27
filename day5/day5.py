#!/usr/bin/env python3
CODE_FRONT = 'F'
CODE_BACK = 'B'
CODE_LEFT = 'L'
CODE_RIGHT = 'R'

MAX_ROWS = 128
MAX_COLS = 8

def convert_binary(s, zero, one):
    return int(s.replace(zero, '0').replace(one, '1'), 2)

def parse(boarding_pass):
    row = convert_binary(boarding_pass[:7], CODE_FRONT, CODE_BACK)
    col = convert_binary(boarding_pass[7:], CODE_LEFT, CODE_RIGHT)
    return (row, col)

def get_seat_id(row, col):
    return (row * 8) + col

def load(file):
    with open(file) as f:
        return [parse(line.strip()) for line in f.readlines()]

def part1(boarding_passes):
    return max(get_seat_id(*boarding_pass) for boarding_pass in boarding_passes)

def part2(boarding_passes):
    last = -1
    for seat_id in sorted(get_seat_id(*boarding_pass) for boarding_pass in boarding_passes):
        if seat_id - last == 2:
            return seat_id - 1
        last = seat_id

def main():
    boarding_passes = load('input.txt')
    value = part1(boarding_passes)
    print(f'Part 1: {value}')
    assert value == 890

    value = part2(boarding_passes)
    print(f'Part 2: {value}')
    assert value == 651

if __name__ == '__main__':
    main()
