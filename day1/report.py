#!/usr/bin/env python3
def main():
    sum = 2020
    with open('expenses.txt') as f:
        vals = [int(line.strip()) for line in f.readlines()]

    memo = set()
    for val in vals:
        result = sum - val
        if result in memo:
            print(f'SUM: {val} + {result} = {val + result}')
            print(f'PRODUCT: {val} * {result} = {val * result}')

        memo.add(val)

if __name__ == '__main__':
    main()
