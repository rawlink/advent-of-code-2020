#!/usr/bin/env python3
from collections import deque

def find_target(numbers):
    data_queue = deque(numbers[:25])
    data_set = set(data_queue)

    for idx, number in enumerate(numbers[25:], 25):
        found = False
        for x in data_queue:
            if (number - x) in data_set and number - x != x:
                found = True
            
        if found:
            to_remove = data_queue.popleft()
            data_set.remove(to_remove)

            data_queue.append(number)
            data_set.add(number)
        else:
            return number

def find_weakness(numbers, target):
    total = 0
    pos = 0
    queue = deque()

    while True and pos < len(numbers):
        if total == target:
            queue_total = sum(queue)
            lowest = highest = queue.pop()
            while len(queue) > 0:
                next = queue.pop()
                lowest = next if next < lowest else lowest
                highest = next if next > highest else highest
            return lowest + highest
        elif total < target:
            val = numbers[pos]
            queue.append(val)
            total += val
            pos += 1
        else:
            val = queue.popleft()
            total -= val


    raise Exception('Weakness for target not found.')

def main():
    with open('ciphertext.txt') as f:
        numbers = [int(line.strip()) for line in f.readlines()]
    
    target = find_target(numbers)
    print(f'Target: {target}')

    weakness = find_weakness(numbers, target)
    print(f'Weakness: {weakness}')

if __name__ == '__main__':
    main()