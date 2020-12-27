#!/usr/bin/env python3
import re

NO_BAGS = 'no other bags'
TARGET = 'shiny gold'

def extract_bag_count(bag_and_count):
    pattern = re.compile('(\\d+) (.*) bags?')
    match = pattern.match(bag_and_count.strip())

    return (match.group(2), int(match.group(1)))

def extract_contained(contained):
    if contained == NO_BAGS:
        return {}

    return {k:v for k,v in (extract_bag_count(value) for value in contained.split(','))}

def parse_line(line):
    bag, contained = line.split(' bags contain ')

    contained = extract_contained(contained)

    return bag, contained

def load(file):
    with open(file) as f:
        lines = [line.strip().strip('.') for line in f.readlines()]
    
    return {k:v for k,v in (parse_line(line) for line in lines)}

def search_adjacencies(node, adjacencies, target, visited, cache):
    if node in visited:
        return False

    visited.add(node)

    if node in cache:
        return cache[node]

    children = adjacencies[node]
    if target in children.keys():
        return True

    for child in children:
        child_result = search_adjacencies(child, adjacencies, target, visited, cache)
        if child_result:
            cache[node] = True
            return True

    return False

def part1(adjacencies, target):
    '''
    >>> part1(load('test1.txt'), TARGET)
    4
    '''
    cache = {}
    total = 0

    for node in adjacencies:
        visited = set()
        found = search_adjacencies(node, adjacencies, target, visited, cache)
        if found:
            total += 1
        cache[node] = found

    return total

def count_children(adjacencies, children, visited, cache):
    total = 0

    for (bag, count) in children.items():
        if bag in visited and not bag in cache:
            raise Exception('We have recursion, a count would be infinite')

        visited.add(bag)

        if bag in cache:
            total += count * cache[bag]
        else:
            child_count_plus_self = count_children(adjacencies, adjacencies[bag], visited, cache) + 1
            total += count * child_count_plus_self
            cache[bag] = child_count_plus_self


    return total

def part2(adjacencies, target):
    '''
    >>> part2(load('test1.txt'), TARGET)
    32
    >>> part2(load('test2.txt'), TARGET)
    126
    '''
    cache = {}
    visited = set()

    total = count_children(adjacencies, adjacencies[target], visited, cache)

    return total

def main():
    adjacencies = load('input.txt')
    value = part1(adjacencies, TARGET)
    print(f'Part 1: {value}')
    assert value == 335

    value = part2(adjacencies, TARGET)
    print(f'Part 2: {value}')
    assert value == 2431

if __name__ == '__main__':
    main()
