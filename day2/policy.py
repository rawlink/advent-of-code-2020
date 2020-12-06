#!/usr/bin/env python3
import re

class Policy:
    def __init__(self, num1, num2, char, password):
        self.num1 = num1
        self.num2 = num2
        self.char = char
        self.password = password

def parse_policies(lines):
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

def sled_policy(policy):
    num_chars = policy.password.count(policy.char)
    return num_chars >= policy.num1 and num_chars <= policy.num2

def toboggan_policy(policy):
    return (policy.password[policy.num1 -1] == policy.char) ^ (policy.password[policy.num2 - 1] == policy.char)

def main():
    with open('passwords.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    policies = parse_policies(lines)

    sled_valid = len(list(filter(sled_policy, policies)))
    toboggan_valid = len(list(filter(toboggan_policy, policies)))

    print(f'Valid sled policies: {sled_valid}')
    print(f'Valid toboggan policies: {toboggan_valid}')

if __name__ == '__main__':
    main()
