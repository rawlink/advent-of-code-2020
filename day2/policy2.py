#!/usr/bin/env python3
import re

def is_valid(pass_policy):
    pattern = re.compile('^(\\d+)-(\\d+) (\\w): (.*)$')
    match = pattern.match(pass_policy)

    if match:
        idx1 = int(match.group(1)) - 1
        idx2 = int(match.group(2)) - 1
        policy_char = match.group(3)
        password = match.group(4)
        if (password[idx1] == policy_char) ^ (password[idx2] == policy_char):
            return True

    return False

def main(input):
    lines = []
    with open(input) as f:
        lines = f.readlines()

    valid = list(filter(is_valid, map(lambda s: s.strip(), lines)))

    print(len(valid))

if __name__ == '__main__':
    main('passwords.txt')
