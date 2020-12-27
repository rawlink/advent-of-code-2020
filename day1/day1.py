#!/usr/bin/env python3
TOTAL = 2020

def load(file):
    with open(file) as f:
        expenses = [int(line.strip()) for line in f.readlines()]

    return expenses

def part1(expenses, sum):
    '''
    >>> part1(load('test1.txt'), TOTAL)
    514579
    '''
    memo = set()
    for expense in expenses:
        diff = sum - expense
        if diff in memo:
            return expense * diff
        memo.add(expense)
    return None

def part2(expenses, sum):
    '''
    >>> part2(load('test1.txt'), TOTAL)
    241861950
    '''
    for idx,expense in enumerate(expenses[:-1]):
        memo = set()
        result = sum - expense

        for expense2 in expenses[idx+1:]:
            result2 = result - expense2

            if result2 in memo:
                return expense * expense2 * result2

            memo.add(expense2)
        memo.add(expense)
    return None

def main():
    expenses = load('input.txt')
    value = part1(expenses, TOTAL)
    print(f'Part 1: {value}')
    assert value == 989824

    value = part2(expenses, TOTAL)
    print(f'Part 2: {value}')
    assert value == 66432240

if __name__ == '__main__':
    main()
