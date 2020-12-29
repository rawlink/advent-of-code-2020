#!/usr/bin/env python3
from collections import deque

def load(file):
    with open(file) as f:
        deck1, deck2 = f.read().split('\n\n')
    
    return [int(card.strip()) for card in deck1.splitlines()[1:]], [int(card.strip()) for card in deck2.splitlines()[1:]]

def calculate_score(cards):
    return sum(i * c for i, c in enumerate(reversed(cards), 1))

def part1(d1, d2):
    '''
    >>> part1(*load('test1.txt'))
    306
    '''
    d1 = deque(d1)
    d2 = deque(d2)

    while len(d1) != 0 and len(d2) != 0:
        c1 = d1.popleft()
        c2 = d2.popleft()

        if c1 > c2:
            d1.extend([c1, c2])
        else:
            d2.extend([c2, c1])

    return calculate_score(d1 if len(d1) > len(d2) else d2)

def part2_recurse(d1, d2):
    d1 = deque(d1)
    d2 = deque(d2)

    round = 1
    hands = set()
    while len(d1) != 0 and len(d2) != 0:
        hand = (tuple(d1), tuple(d2))
        if hand in hands:
            return 0, True
        else:
            hands.add(hand)

        c1 = d1.popleft()
        c2 = d2.popleft()

        if len(d1) >= c1 and len(d2) >= c2:
            # recurse
            _, one_wins = part2_recurse(list(d1)[:c1], list(d2)[:c2])
            if one_wins:
                d1.extend([c1, c2])
            else:
                d2.extend([c2, c1])
        else:
            if c1 > c2:
                d1.extend([c1, c2])
            else:
                d2.extend([c2, c1])
        round += 1

    return calculate_score(d1 if len(d1) > len(d2) else d2), len(d1) > len(d2)

def part2(d1, d2):
    '''
    >>> part2(*load('test1.txt'))
    291
    '''

    return part2_recurse(d1, d2)[0]

def main():
    deck1, deck2 = load('input.txt')
    value = part1(deck1, deck2)
    print(f'Part 1: {value}')
    assert value == 31629

    value = part2(deck1, deck2)
    print(f'Part 2: {value}')
    assert value == 35196

if __name__ == '__main__':
    main()