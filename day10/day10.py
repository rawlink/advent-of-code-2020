#!/usr/bin/env python3
from collections import deque

def part1(adapters):
    distribution = [0,0,0]
    last = adapters[0]

    for adapter in adapters[1:]:
        diff = adapter - last
        distribution[diff - 1] += 1
        last = adapter
    
    return distribution[0] * distribution[2]

def part2(adapters):
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

def load(file):
    with open(file) as f:
        adapters = [int(line.strip()) for line in f.readlines()]
    adapters.append(0)
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    return adapters
    
def main():
    adapters = load('test1.txt')
    result = part1(adapters)
    print(f'Test 1 jolt product: {result}')
    assert result == 35
    result = part2(adapters)
    print(f'Test 1 jolt combos: {result}')
    assert result == 8

    adapters = load('test2.txt')
    result = part1(adapters)
    print(f'Test 2 jolt product: {result}')
    assert result == 220
    result = part2(adapters)
    print(f'Test 2 jolt combos: {result}')
    assert result == 19208

    adapters = load('input.txt')
    print(f'Jolt product: {part1(adapters)}')
    print(f'Jolt combos: {part2(adapters)}')

if __name__ == '__main__':
    main()