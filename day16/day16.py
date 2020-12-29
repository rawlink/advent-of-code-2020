#!/usr/bin/env python3
from math import prod
from functools import reduce

def parse_rule(rule):
    name, ranges = rule.split(':')
    name = name.strip()
    ranges = ranges.split('or')
    ranges = [tuple(map(int, range.split('-'))) for range in ranges] #assuming ranges are always (min,max)

    return name, ranges

def parse_ticket(ticket):
    return list(map(int, ticket.split(',')))

def load(file):
    with open(file) as f:
        rules, mine, others = [block.split('\n') for block in f.read().split('\n\n')]

    rules = {k:v for k,v in (parse_rule(rule) for rule in rules)}
    mine = parse_ticket(mine[1])
    others = [parse_ticket(ticket) for ticket in others[1:] if ticket.strip()]
    
    return rules, mine, others

def passes_rules(rules, value):
    return any([any(map(lambda range: range[0] <= value <= range[1], ranges)) for ranges in rules.values()])

# Would be faster if the rules were consolidated into contiguous ranges. Too lazy. So much looping in this one.
def part1(rules, others):
    '''
    >>> part1(*load('test1.txt')[::2])
    (71, [[7, 3, 47]])
    '''
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

    return prod(mine[idx] for idx, column_name in enumerate(column_names) if 'departure' in column_name)

def main():
    rules, mine, others = load('input.txt')
    value, valid = part1(rules, others)
    print(f'Part 1: {value}')
    assert value == 20048

    value = part2(rules, mine, valid)
    print(f'Part 2: {value}')
    assert value == 4810284647569

if __name__ == '__main__':
    main()