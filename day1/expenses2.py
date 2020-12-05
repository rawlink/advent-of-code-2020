#!/usr/bin/env python3
def main(input, sum):
    with open(input) as f:
        lines = f.readlines()

        vals = [int(x.strip()) for x in lines]

        for idx,val in enumerate(vals[:-1]):
            memo = set()
            result = sum - val

            for val2 in vals[idx+1:]:
                result2 = result - val2

                if result2 in memo:
                    print(f'SUM: {val} + {val2} + {result2} = {val + val2 + result2}')
                    print(f'PRODUCT: {val} * {val2} + {result2} = {val * val2 * result2}')
                    exit()

                memo.add(val2)
            memo.add(val)

if __name__ == '__main__':
    main('expenses.txt', 2020)
