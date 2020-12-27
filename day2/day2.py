#!/usr/bin/env python3
import re

class Policy:
    def __init__(self, num1, num2, char, password):
        self.num1 = num1
        self.num2 = num2
        self.char = char
        self.password = password

def load(file):
    with open(file) as f:
        lines = [line.strip() for line in f.readlines()]

    policies = []
    pattern = re.compile('^(\\d+)-(\\d+) (\\w): (.*)$')

    for line_num, line in enumerate(lines):
        match = pattern.match(line)

        if not match:
            raise Exception(f'Invalid policy in line #{line_num}: {line}')

        num1 = int(match.group(1))
        num2 = int(match.group(2))
        char = match.group(3)
        password = match.group(4)
        policies.append(Policy(num1, num2, char, password))

    return policies

def part1(policies):
    '''
    >>> part1(load('test1.txt'))
    2
    '''
    count = 0
    for policy in policies:
        num_chars = policy.password.count(policy.char)
        if num_chars >= policy.num1 and num_chars <= policy.num2:
            count += 1
    return count


def part2(policies):
    '''
    >>> part2(load('test1.txt'))
    1
    '''
    count = 0
    for policy in policies:
        if (policy.password[policy.num1 -1] == policy.char) ^ (policy.password[policy.num2 - 1] == policy.char):
            count += 1
    return count


def main():
    policies = load('input.txt')
    value = part1(policies)
    print(f'Part 1: {value}')
    assert value == 410


    value = part2(policies)
    print(f'Part 2: {value}')
    assert value == 694

if __name__ == '__main__':
    main()
