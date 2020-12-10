#!/usr/bin/env python3
def main():
    with open('customs.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    declarations = set()
    total_declarations = 0

    for line in lines:
        if len(line) == 0:
            print(f'Group total: {len(declarations)}')
            total_declarations += len(declarations)
            declarations = set()
            continue
        else:
            for c in line:
                declarations.add(c)
    
    total_declarations += len(declarations)

    print(f'Total declarations: {total_declarations}')

if __name__ == '__main__':
    main()
