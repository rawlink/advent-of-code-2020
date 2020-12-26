#!/usr/bin/env python3
import math

SUBJECT = 7
PRIME = 20201227 # Good example of insufficiently large prime for Diffie-Hellman

def part1(pub1, pub2):
    value = 1
    sec1 = 0
    while value != pub1:
        value = (SUBJECT * value) % PRIME
        sec1 += 1

    enc = 1
    for _ in range(sec1):
        enc = (pub2 * enc) % PRIME

    return enc

# This is how Diffie-Hellman works (https://dzone.com/articles/diffie-hellman-key-exchange-2).
def main():
    value = part1(5764801, 17807724)
    print(f'Test 1 - Part 1: {value}')
    assert value == 14897079

    value = part1(12232269, 19452773)
    print(f'Part 1: {value}')

if __name__ == '__main__':
    main()