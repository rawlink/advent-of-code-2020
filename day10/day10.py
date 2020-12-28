#!/usr/bin/env python3
from collections import deque

def load(file):
    with open(file) as f:
        adapters = [int(line.strip()) for line in f.readlines()]
    adapters.append(0)
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    return adapters

def part1(adapters):
    '''
    >>> part1(load('test1.txt'))
    35
    >>> part1(load('test2.txt'))
    220
    '''
    distribution = [0,0,0]
    last = adapters[0]

    for adapter in adapters[1:]:
        distribution[adapter - last - 1] += 1
        last = adapter
    
    return distribution[0] * distribution[2]

def part2(adapters):
    '''
    >>> part2(load('test1.txt'))
    8
    >>> part2(load('test2.txt'))
    19208
    '''
    acc = deque()
    acc.append([adapters[0], 1])
    for adapter in adapters[1:]:
        acc.append([adapter, acc[-1][1]])
        acc_len  = len(acc)

        # UGLY - consider using a class for accumulator members
        if acc_len > 2 and adapter - acc[-3][0] <= 3:
            acc[-1][1] += acc[-3][1]

        if acc_len > 3 and adapter - acc[-4][0] <= 3:
            acc[-1][1] += acc[-4][1]

        while len(acc) > 4:
            acc.popleft()

    return acc[-1][1]
    
def main():
    adapters = load('input.txt')
    value = part1(adapters)
    print(f'Part 1: {value}')
    assert value == 2470

    value = part2(adapters)
    print(f'Part 2: {value}')
    assert value == 1973822685184

if __name__ == '__main__':
    main()