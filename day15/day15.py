#!/usr/bin/env python3
PART1_TARGET = 2020
PART2_TARGET = 30000000

def part1(numbers, target):
    '''
    >>> part1([0,3,6], 10)
    0
    >>> part1([0,3,6], PART2_TARGET)
    175594
    >>> part1([1,3,2], PART1_TARGET)
    1
    >>> part1([1,3,2], PART2_TARGET)
    2578
    >>> part1([2,1,3], PART1_TARGET)
    10
    >>> part1([2,1,3], PART2_TARGET)
    3544142
    >>> part1([1,2,3], PART1_TARGET)
    27
    >>> part1([1,2,3], PART2_TARGET)
    261214
    >>> part1([2,3,1], PART1_TARGET)
    78
    >>> part1([2,3,1], PART2_TARGET)
    6895259
    >>> part1([3,2,1], PART1_TARGET)
    438
    >>> part1([3,2,1], PART2_TARGET)
    18
    >>> part1([3,1,2], PART1_TARGET)
    1836
    >>> part1([3,1,2], PART2_TARGET)
    362
    '''
    memory = {}

    for idx, number in enumerate(numbers[:-1]):
        memory[number] = idx

    last = numbers[-1]
    last_pos = len(numbers) -1

    for pos in range(len(numbers), target):
        if last in memory:
            old_last = last
            last = last_pos - memory[last]
            memory[old_last] = last_pos
        else:
            memory[last] = last_pos
            last = 0
        last_pos = pos

    return last

def main():
    data = [1,17,0,10,18,11,6]

    value = part1(data, PART1_TARGET)
    print(f'Part 1: {value}')
    assert value == 595

    value = part1(data, PART2_TARGET)
    print(f'Part 2: {value}')
    assert value == 1708310

if __name__ == '__main__':
    main()