#!/usr/bin/env python3
def parse_rule(rule):
    key, value = rule.split(':')
    pos = value.find('"')
    if pos >= 0:
        value = value[pos + 1]
    else:
        value = [e.strip().split() for e in (sub for sub in value.split('|'))]

    return key.strip(), value

def load(file):
    with open(file) as f:
        rules,messages = f.read().split('\n\n')

    rules = {key:value for key,value in (parse_rule(rule) for rule in rules.splitlines())}
    messages = [message.strip() for message in messages.splitlines()]

    return rules, messages

def match_rules(message, rules, sequence):
    if not message or not sequence:
        return not message and not sequence
    
    # Get subsequences for first item in sequence
    subsequences = rules[sequence[0]]

    if isinstance(subsequences, list): # Not a terminal rule
        for subsequence in subsequences:
            subsequence = subsequence.copy()
            subsequence.extend(sequence[1:])
            found = match_rules(message, rules, subsequence)
            if found:
                return True
    elif message[0] == subsequences: # A terminal rule
        return match_rules(message[1:], rules, sequence[1:])

    return False

def part1(rules, messages):
    total = 0
    for message in messages:
        if match_rules(message, rules, ['0']):
            total += 1
    
    return total

def part2(rules, messages):
    patch = ['8: 42 | 42 8', '11: 42 31 | 42 11 31']
    for rule in patch:
        key, value = parse_rule(rule)
        rules[key] = value
    
    # pass things into part1 and hope that everything still works
    return part1(rules, messages)


# Ugggh. This one is ugly :-/. I'm not proud of the readability (or lack thereof). It took forever to get the recursion
# to work correctly. I'm sure there is a better way.
def main():
    rules, messages = load('test1.txt')
    value = part1(rules, messages)
    print(f'Test 1 - Part 1: {value}')
    assert value == 2

    rules, messages = load('input.txt')
    value = part1(rules, messages)
    print(f'Part 1: {value}')
    value = part2(rules, messages)
    print(f'Part 2: {value}')

if __name__ == '__main__':
    main()