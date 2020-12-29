#!/usr/bin/env python3
import re

def parse(line):
    [ingredients, allergens] = line.split(' (contains ')
    ingredients = set(ingredient.strip() for ingredient in ingredients.strip().split())
    allergens = set(allergen.strip() for allergen in allergens.rstrip(')').split(','))

    return (allergens, ingredients)

def load(file):
    with open(file) as f:
        lines = [line.strip() for line in f.readlines()]

    data = [parse(line) for line in lines]

    return data

def map_allergens(data):
    possibilities = {}

    for allergens, ingredients in data:
        for allergen in allergens:
            if allergen not in possibilities:
                possibilities[allergen] = set(ingredients)
            else:
                possibilities[allergen] &= ingredients

    return possibilities

def part1(data):
    '''
    >>> part1(load('test1.txt'))
    5
    '''
    possibilities = map_allergens(data)
    all_possibilities = set(possible for ingredients in possibilities.values() for possible in ingredients)

    total = 0
    for _, ingredients in data:
        for ingredient in ingredients:
            if ingredient not in all_possibilities:
                total += 1

    return total

def part2(data):
    '''
    >>> part2(load('test1.txt'))
    'mxmxvkd,sqjhc,fvjkl'
    '''
    # This function destructively modifies possibilities... That's fine for this task.
    possibilities = map_allergens(data)
    singles = set()

    while len(singles) < len(possibilities):
        to_remove = set()
        for allergen, ingredients in possibilities.items():
            if len(ingredients) == 1:
                single = next(iter(ingredients))
                if single not in singles:
                    to_remove.add(single)

        singles |= to_remove

        for _, ingredients in possibilities.items():
           if(len(ingredients) > 1):
               ingredients -= to_remove

    return ','.join(next(iter(possibilities[allergen])) for allergen in sorted(possibilities.keys()))

def main():
    ingredients = load('input.txt')
    value = part1(ingredients)
    print(f'Part 1: {value}')
    assert value == 1930

    value = part2(ingredients)
    print(f'Part 2: {value}')
    assert value == 'spcqmzfg,rpf,dzqlq,pflk,bltrbvz,xbdh,spql,bltzkxx'

if __name__ == '__main__':
    main()