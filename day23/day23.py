#!/usr/bin/env python3

def get_seg_info(ring, start, n):
    if n < 1:
        raise Exception('n must be > 0')
    curr = start
    prev = start
    members = set()
    for _ in range(n):
        members.add(curr)
        prev = curr
        curr = ring[curr]

    return members, prev, curr

def create_ring(data):
    first = data[0]
    ring = [0] * (len(data) + 1)

    curr = first

    for cup in data[1:]:
        ring[curr] = cup
        curr = cup

    ring[curr] = first

    return ring

def play(ring, start, high, iterations):
    curr = start

    for _ in range(iterations):
        next = ring[curr]
        seg_members, seg_tail, seg_tail_next = get_seg_info(ring, next, 3)
        ins = curr - 1 if curr > 1 else high
        while ins in seg_members:
            ins = ins - 1 if ins > 1 else high

        ins_next = ring[ins]
        ring[curr] = seg_tail_next
        ring[ins] = next
        ring[seg_tail] = ins_next
        curr = ring[curr]

def part1(data):
    iterations = 100
    high = max(data)
    ring = create_ring(data)
    values = play(ring, data[0], high, iterations)

    result = []
    curr = 1

    for _ in range(len(data) - 1):
        next = ring[curr]
        result.append(str(next))
        curr = next

    return ''.join(result)

def part2(data):
    cups = 1000000
    iterations = 10000000
    high = max(data)
    larger_data = list(range(1, cups + 1))
    for idx, val in enumerate(data):
        larger_data[idx] = val
    ring = create_ring(larger_data)
    high = cups
    play(ring, data[0], high, iterations)

    return ring[1] * ring[ring[1]]


def main():
    value = part1([3, 8, 9, 1, 2, 5, 4, 6, 7])
    print(f'Test 1 - Part 1: {value}')
    assert value == '67384529'
    value = part2([3, 8, 9, 1, 2, 5, 4, 6, 7])
    print(f'Test 1 - Part 2: {value}')
    assert value == 149245887792

    value = part1([8, 7, 1, 3, 6, 9, 4, 5, 2])
    print(f'Part 1: {value}')
    value = part2([8, 7, 1, 3, 6, 9, 4, 5, 2])
    print(f'Part 2: {value}')

if __name__ == '__main__':
    main()