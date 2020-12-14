#!/usr/bin/env python3
from functools import reduce

class RemainderInfo:
    def __init__(self, n, b):
        self.n = n
        self.b = b
        self.N = 0
        self.x = 0

    # Adding 'stringy' methods for debugging correctness of implementation.
    def __str__(self):
        return f'n: {self.n}, b: {self.b}, N: {self.N}, x: {self.x}'

    def __repr__(self):
        return f'RemainderInfo(n: {self.n}, b: {self.b}, N: {self.N}, x: {self.x})'

def load(file):
    with open(file) as f:
        lines = [line.strip() for line in f.readlines()]
    
    if len(lines) != 2:
        raise Exception('Input file must only contain two lines: {file}')

    timestamp = int(lines[0])
    buses = [int(x) if x != 'x' else -1 for x in lines[1].split(',')]

    return timestamp, buses

def minutes_til_bus(timestamp, bus):
    return bus - (timestamp % bus)

def part1(timestamp, buses):
    bus_to_catch = buses[0]
    bus_to_catch_wait = minutes_til_bus(timestamp, bus_to_catch)

    for bus in buses[1:]:
        if bus <= 0:
            continue
        wait = minutes_til_bus(timestamp, bus)
        if wait < bus_to_catch_wait:
            bus_to_catch = bus
            bus_to_catch_wait = wait

    return bus_to_catch * bus_to_catch_wait

def part2(buses):
    # A quick visual inspection of the dataset shows that the bus numbers are all prime. We'll take advantage of that.
    # If they are at least co-prime, we can use Chinese Remainder Theorem - https://www.youtube.com/watch?v=zIFehsBHB8o
    start = 0
    for idx, bus in enumerate(buses):
        if bus > 0:
            start = idx
            break

    ris = []
    N = 1
    num_buses = len(buses)
    for idx, bus in enumerate(buses[start:]):
        if bus <= 0:
            continue

        # We need to start our numbering at 1 for Chinese Remainder Theorom to work.
        # The lowest remainder must be 1 in order for Chinese Remainder Theorem to work ( divide by zero and all that),
        # so we need to be 1-indexed in our remainders. *BUT*, that means the number that needs to have a remainder of 1
        # is our last valid bus. Then the prior bus will come x1 additional timestamps earlier resulting in a remainder of
        # 1 + x1. The next at x2 additional steps from the bus before it resulting in a remainder of 1 + x1 + x2, etc.
        # That means that at the end of this, the result needs to have the remainder_max substracted from it.
        ris.append(RemainderInfo(bus, num_buses - idx))
        N *= bus

    for ri in ris:
        ri.N = N // ri.n

        rem = ri.N % ri.n

        if rem == 1:
            ri.x = 1
            continue

        found = False
        for mult in range(1, ri.n):
            if (rem * mult) % ri.n == 1:
                found = True
                break

        if not found:
            raise Exception('Unable to find an appropriate remainder.')

        ri.x = mult

    result = reduce(lambda a, b: a + (b.b * b.N * b.x), ris, 0)
    result %= N
    result -= num_buses # Subtracting remainder_max as stated in a prior comment. 

    return result

def main():
    timestamp, buses = load('test1.txt')
    result = part1(timestamp, buses)
    print(f'Test 1 - Part 1: {result}')
    assert result == 295
    result = part2(buses)
    print(f'Test 1 - Part 2: {result}')
    assert result == 1068781

    timestamp, buses = load('input.txt')
    result = part1(timestamp, buses)
    print(f'Part 1: {result}')
    result = part2(buses)
    print(f'Part 2: {result}')


if __name__ == '__main__':
    main()