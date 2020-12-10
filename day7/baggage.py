#!/usr/bin/env python3
import re

ADJACENCY_KV_SEPARATER = ' contain '
NO_BAGS = 'no other bags'
TARGET = 'bright gold'

def extract_key(key):
    pattern = re.compile('(.*) bags')
    match = pattern.match(key.strip())
    return match.group(1)

def extract_values(raw_value):
    if raw_value == NO_BAGS:
        return {}

    value_parts = raw_value.split(',')
    values = {}
    for value_part in value_parts:
        (bag, count) = extract_value(value_part)
        values[bag] = count
    return values

def extract_value(value):
    pattern = re.compile('(\\d+) (.*) bags*')
    match = pattern.match(value.strip())

    return (match.group(2), int(match.group(1)))

def create_adjacencies(lines):
    adjacencies = {}
    for line in lines:
        parts = line.split(ADJACENCY_KV_SEPARATER)

        if len(parts) != 2:
            raise Exception(f'ABORTING - KV split failure (length {len(parts)} should be 2)')

        [key, values_part] = parts

        key = extract_key(key)

        values = extract_values(values_part)

        adjacencies[key] = values

    return adjacencies

def search_adjacencies(adjacencies, target):
    print('Counting candidates.')
    cache = {}

    total = 0

    for node in adjacencies:
        visited = set()
        found = search_adjacencies_recurse(node, adjacencies, target, visited, cache)
        if found:
            total += 1
        cache[node] = found

    return total

def search_adjacencies_recurse(node, adjacencies, target, visited, cache):
    if node in visited:
        return False

    visited.add(node)

    if node in cache:
        return cache[node]

    children = adjacencies[node]
    if target in children.keys():
        return True

    for child in children:
        child_result = search_adjacencies_recurse(child, adjacencies, target, visited, cache)
        if child_result:
            cache[node] = True
            return True

    return False

def count_children(adjacencies, target):
    print('Counting sub-bags.')
    cache = {}
    visited = set()

    total = count_children_recurse(adjacencies, adjacencies[target], visited, cache)

    return total

def count_children_recurse(adjacencies, children, visited, cache):
    total = 0

    for (bag, count) in children.items():
        if bag in visited and not bag in cache:
            raise Exception('We have recursion, a count would be infinite')

        visited.add(bag)

        if bag in cache:
            total += count * cache[bag]
        else:
            child_count_plus_self = count_children_recurse(adjacencies, adjacencies[bag], visited, cache) + 1
            total += count * child_count_plus_self
            cache[bag] = child_count_plus_self


    return total

def main():
    target = 'shiny gold'

    # Tests
    with open('test_rules_1.txt') as f:
        lines = [line.strip().strip('.') for line in f.readlines()]
    adjacencies = create_adjacencies(lines)
    contained_total = count_children(adjacencies, target)
    print(f'Test 1 - Total child bags(expect 32): {contained_total}')

    with open('test_rules_2.txt') as f:
        lines = [line.strip().strip('.') for line in f.readlines()]
    adjacencies = create_adjacencies(lines)
    contained_total = count_children(adjacencies, target)
    print(f'Test 2 - Total child bags(expect 126): {contained_total}')

    # Actual data
    with open('rules.txt') as f:
        lines = [line.strip().strip('.') for line in f.readlines()]

    adjacencies = create_adjacencies(lines)

    container_total = search_adjacencies(adjacencies, target)
    print(f'Total candidate bags: {container_total}')

    contained_total = count_children(adjacencies, target)
    print(f'Total child bags: {contained_total}')


if __name__ == '__main__':
    main()
