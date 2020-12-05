#!/usr/bin/env python3
def main(input, sum):
    with open(input) as f:
        lines = f.readlines()

        vals = [int(x.strip()) for x in lines]

        memo = set()
        for val in vals:
            result = sum - val

            if result in memo:
                print(f'SUM: {val} + {result} = {val + result}')
                print(f'PRODUCT: {val} * {result} = {val * result}')
                exit()

            memo.add(val)

if __name__ == '__main__':
    main('expenses.txt', 2020)
