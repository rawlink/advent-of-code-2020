#!/usr/bin/env python3
def load(file):
    with open(file) as f:
        return [line.split() for line in f.read().split('\n\n')]

def part2(groups):
    '''
    >>> part2(load('test1.txt'))
    6
    '''
    group_declarations = []
    for group in groups:
        declarations = set(group[0])
        for declaration in group[1:]:
            declarations &= set(declaration)
        group_declarations.append(declarations)
    
    return sum(len(declarations) for declarations in group_declarations)

def part1(groups):
    '''
    >>> part1(load('test1.txt'))
    11
    '''
    group_declarations = []
    for group in groups:
        declarations = set(declaration for declarations in group for declaration in list(declarations))
        group_declarations.append(declarations)
    
    return sum(len(declarations) for declarations in group_declarations)

def main():
    groups = load('input.txt')
    value = part1(groups)
    print(f'Part 1: {value}')
    assert value == 6259

    value = part2(groups)
    print(f'Part 2: {value}')
    assert value == 3178

if __name__ == '__main__':
    main()
