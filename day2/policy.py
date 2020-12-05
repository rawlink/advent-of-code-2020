#!/usr/bin/env python3
import re

def is_valid(pass_policy):
    pattern = re.compile('^(\\d+)-(\\d+) (\\w): (.*)$')
    match = pattern.match(pass_policy)

    if match:
        min = int(match.group(1))
        max = int(match.group(2))
        policy_char = match.group(3)
        password = match.group(4)
        num_chars = password.count(policy_char)
        if num_chars >= min and num_chars <= max:
            return True

    return False

def main(input):
    with open(input) as f:
        lines = [line.strip() for line in f.readlines()]

    valid = list(filter(is_valid, map(lambda s: s.strip(), lines)))

    print(len(valid))

if __name__ == '__main__':
    main('passwords.txt')
