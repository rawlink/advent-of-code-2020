#!/usr/bin/env python3
from collections import deque

def distribution_product(numbers):
    distribution = [0,0,0]
    last = numbers[0]

    for number in numbers[1:]:
        diff = number - last
        distribution[diff - 1] += 1
        last = number
    
    return distribution[0] * distribution[2]

def combos(numbers):
    acc = deque()
    acc.append([numbers[0], 1])
    for number in numbers[1:]:
        acc.append([number, acc[-1][1]])
        acc_len  = len(acc)

        # UGLY - consider using a class for accumulator members
        if acc_len > 2 and number - acc[-3][0] <= 3:
            acc[-1][1] += acc[-3][1]

        if acc_len > 3 and number - acc[-4][0] <= 3:
            acc[-1][1] += acc[-4][1]

        while len(acc) > 4:
            acc.popleft()

    return acc[-1][1]

def load(file):
    with open(file) as f:
        numbers = [int(line.strip()) for line in f.readlines()]
    numbers.append(0)
    numbers.sort()
    numbers.append(numbers[-1] + 3)
    return numbers
    
def main():
    numbers = load('test1.txt')
    test_val = distribution_product(numbers)
    print(f'Test 1 jolt product: {test_val}')
    assert test_val == 35
    test_val = combos(numbers)
    print(f'Test 1 jolt combos: {test_val}')
    assert test_val == 8

    numbers = load('test2.txt')
    test_val = distribution_product(numbers)
    print(f'Test 2 jolt product: {test_val}')
    assert test_val == 220
    test_val = combos(numbers)
    print(f'Test 2 jolt combos: {test_val}')
    assert test_val == 19208

    numbers = load('input.txt')
    print(f'Jolt product: {distribution_product(numbers)}')
    print(f'Jolt combos: {combos(numbers)}')

if __name__ == '__main__':
    main()