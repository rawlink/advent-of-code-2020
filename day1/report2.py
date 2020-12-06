#!/usr/bin/env python3
def main():
    sum = 2020
    with open('expenses.txt') as f:
        vals = [int(line.strip()) for line in f.readlines()]

    for idx,val in enumerate(vals[:-1]):
        memo = set()
        result = sum - val

        for val2 in vals[idx+1:]:
            result2 = result - val2

            if result2 in memo:
                print(f'SUM: {val} + {val2} + {result2} = {val + val2 + result2}')
                print(f'PRODUCT: {val} * {val2} + {result2} = {val * val2 * result2}')

            memo.add(val2)
        memo.add(val)

if __name__ == '__main__':
    main()
