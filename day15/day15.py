#!/usr/bin/env python3
TEST1_DATA = [0,3,6]
TEST2_DATA = [1,3,2]
TEST3_DATA = [2,1,3]
TEST4_DATA = [1,2,3]
TEST5_DATA = [2,3,1]
TEST6_DATA = [3,2,1]
TEST7_DATA = [3,1,2]

DATA = [1,17,0,10,18,11,6]


def part1(numbers, target):
    memory = {}

    for idx, number in enumerate(numbers[:-1]):
        memory[number] = idx

    last = numbers[-1]
    last_pos = len(numbers) -1

    for pos in range(len(numbers), target):
        if last in memory:
            old_last = last
            last = last_pos - memory[last]
            memory[old_last] = last_pos
        else:
            memory[last] = last_pos
            last = 0
        last_pos = pos

    return last

def main():
    part1_target = 2020
    part2_target = 30000000

    value = part1(TEST1_DATA, 10)
    print(f'TEST 1 - PART 1: {value}')
    assert value == 0
    value = part1(TEST1_DATA, part2_target)
    print(f'TEST 1 - PART 2: {value}')
    assert value == 175594

    value = part1(TEST2_DATA, part1_target)
    print(f'TEST 2 - PART 1: {value}')
    assert value == 1
    value = part1(TEST2_DATA, part2_target)
    print(f'TEST 1 - PART 2: {value}')
    assert value == 2578

    value = part1(TEST3_DATA, part1_target)
    print(f'TEST 3 - PART 1: {value}')
    assert value == 10
    value = part1(TEST3_DATA, part2_target)
    print(f'TEST 1 - PART 2: {value}')
    assert value == 3544142

    value = part1(TEST4_DATA, part1_target)
    print(f'TEST 4 - PART 1: {value}')
    assert value == 27
    value = part1(TEST4_DATA, part2_target)
    print(f'TEST 1 - PART 2: {value}')
    assert value == 261214

    value = part1(TEST5_DATA, part1_target)
    print(f'TEST 5 - PART 1: {value}')
    assert value == 78
    value = part1(TEST5_DATA, part2_target)
    print(f'TEST 1 - PART 2: {value}')
    assert value == 6895259

    value = part1(TEST6_DATA, part1_target)
    print(f'TEST 6 - PART 1: {value}')
    assert value == 438
    value = part1(TEST6_DATA, part2_target)
    print(f'TEST 1 - PART 2: {value}')
    assert value == 18

    value = part1(TEST7_DATA, part1_target)
    print(f'TEST 7 - PART 1: {value}')
    assert value == 1836
    value = part1(TEST7_DATA, part2_target)
    print(f'TEST 1 - PART 2: {value}')
    assert value == 362

    value = part1(DATA, part1_target)
    print(f'PART 1: {value}')
    value = part1(DATA, part2_target)
    print(f'PART 2: {value}')

if __name__ == '__main__':
    main()