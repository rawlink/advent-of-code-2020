#!/usr/bin/env python3
from collections import deque

def load(file):
    with open(file) as f:
        return [int(line.strip()) for line in f.readlines()]

def part1(numbers, preamble):
    '''
    >>> part1(load('test1.txt'), 5)
    127
    '''
    data_queue = deque(numbers[:preamble])
    data_set = set(data_queue)

    for idx, number in enumerate(numbers[preamble:], preamble):
        if any((number -x in data_set and number - x != x) for x in data_queue):
            to_remove = data_queue.popleft()
            data_set.remove(to_remove)
            data_queue.append(number)
            data_set.add(number)
        else:
            return number

def part2(numbers, target):
    '''
    >>> part2(load('test1.txt'), 127)
    62
    '''
    total = 0
    queue = deque()

    for number in numbers:
        if total == target:
            lowest = min(queue)
            highest = max(queue)
            return lowest + highest

        queue.append(number)
        total += number

        while total > target:
            total -= queue.popleft()


    raise Exception('Weakness for target not found.')

def main():
    numbers = load('input.txt')
    value = part1(numbers, 25)
    print(f'Part 1: {value}')
    assert value == 3199139634

    value = part2(numbers, value)
    print(f'Weakness: {value}')
    assert value == 438559930

if __name__ == '__main__':
    main()