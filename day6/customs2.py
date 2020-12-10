#!/usr/bin/env python3
def group_total(choices, num):
    total = 0
    for (key,val) in choices.items():
        if val == num:
            total += 1

    return total
    
def main():
    with open('customs.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    declarations = {}
    num_in_group = 0
    total_declarations = 0

    for line in lines:
        if len(line) == 0:
            num_declarations = group_total(declarations, num_in_group)
            print(f'Group total: {num_declarations}')
            total_declarations += num_declarations
            declarations = {}
            num_in_group = 0
            continue
        else:
            num_in_group += 1
            for c in line:
                if not c in declarations:
                    declarations[c] = 1
                else:
                    declarations[c] += 1
    
    total_declarations += group_total(declarations, num_in_group)

    print(f'Total declarations: {total_declarations}')

if __name__ == '__main__':
    main()
