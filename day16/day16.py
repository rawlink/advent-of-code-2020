#!/usr/bin/env python3
from math import prod
from functools import reduce

def load(file):
    with open(file) as f:
        lines = [line.strip() for line in f.readlines()]

    rules = {}
    # Assuming the file is formatted perfectly. No guardrails.
    for idx,line in enumerate(lines):
        if not line:
            break
        name, ranges = line.split(':')
        ranges = ranges.split('or')
        ranges = [tuple(map(int, range.split('-'))) for range in ranges] #assuming ranges are always (min,max)
        rules[name.strip()] = ranges

    idx += 2
    mine = [int(num) for num in lines[idx].split(',')]

    idx += 3
    others = [list(map(int, line.split(','))) for line in lines[idx:]]
    
    return rules, mine, others

def passes_rules(rules, value):
    return any([any(map(lambda range: range[0] <= value <= range[1], ranges)) for ranges in rules.values()])

# Would be faster if the rules were consolidated into contiguous ranges. Too lazy. So much looping in this one.
def part1(rules, others):
    total = 0
    valid = []
    for values in others:
        bad = False
        for value in values:
            if not passes_rules(rules, value):
                total += value
                bad = True
        if not bad:
            valid.append(values)

    return total, valid

def filter_possibilities(rules, possibles, value):
    not_possible = []
    for possible in possibles:
        match = any(map(lambda range: range[0] <= value <= range[1], rules[possible]))
        
        if not match:
            not_possible.append(possible)
    
    possibles.difference_update(not_possible)

def resolve_possibilities(possibilities):
    # The following assumes there is a solution. Bad/insufficient data would probably result in infinite loops.
    single_names = set()
    while len(single_names) < len(possibilities):
        to_remove = set()
        for possibility in possibilities:
            if len(possibility) == 1:
                single = next(iter(possibility))
                if single not in single_names:
                    to_remove.add(single)

        single_names.update(to_remove)

        for possibility in possibilities:
           if(len(possibility) > 1):
               possibility.difference_update(to_remove)

    return [next(iter(possibility)) for possibility in possibilities]

def part2(rules, mine, valid):
    possible_column_names = [set(rules.keys()) for _ in range(len(mine))]

    for values in valid:
        for idx,value in enumerate(values):
            filter_possibilities(rules, possible_column_names[idx], value)

    column_names = resolve_possibilities(possible_column_names)

    prod = 1
    for idx,column_name in enumerate(column_names):
        if 'departure' in column_name:
            prod *= mine[idx]

    return prod

def main():
    rules, mine, others = load('test1.txt')
    value, _ = part1(rules, others)
    print(f'Test 1 - Part 1: {value}')
    assert value == 71

    rules, mine, others = load('input.txt')
    value, valid = part1(rules, others)
    print(f'Part 1: {value}')
    value = part2(rules, mine, valid)
    print(f'Part 2: {value}')

if __name__ == '__main__':
    main()