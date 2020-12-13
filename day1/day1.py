#!/usr/bin/env python3

def load(file):
    with open(file) as f:
        expenses = [int(line.strip()) for line in f.readlines()]
    
    return expenses

def part1(expenses, sum):
    memo = set()
    for expense in expenses:
        result = sum - expense
        if result in memo:
            return expense * result
        memo.add(expense)
    return None

def part2(expenses, sum):
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
    sum = 2020

    expenses = load('test1.txt')
    product = part1(expenses, sum)
    print(f'Test1 - Part 1 product: {product}')
    assert product == 514579
    product = part2(expenses, sum)
    print(f'Test1 - Part 2 product: {product}')
    assert product == 241861950

    expenses = load('input.txt')
    product = part1(expenses, sum)
    print(f'Part 1 product: {product}')
    product = part2(expenses, sum)
    print(f'Part 2 product: {product}')
    
if __name__ == '__main__':
    main()
