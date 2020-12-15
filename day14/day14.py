#!/usr/bin/env python3
import re
from itertools import product

ONE = '1'
ZERO = '0'
EX = 'X'
FLOATING_BIT = '{}'

MASK_INSTRUCTION = re.compile('^mask = (.+)$')
MEM_INSTRUCTION = re.compile('^mem\\[(\\d+)\\] = (\\d+)$')

class Mask:
    def __init__(self, mask):
        if re.compile('^[10X]{36}$').match(mask) is None:
            raise Exception(f'Masks must be 36 chars and only contain 1, 0, or X. Invalid Mask: {mask}')

        self.x_as_ones = int(mask.replace(EX, ONE), 2)
        self.x_as_zeros = int(mask.replace(EX, ZERO), 2)
        self.num_floating_bits = mask.count(EX)
        self.template = mask.replace(ZERO, ONE).replace(EX, FLOATING_BIT)

    def apply_value_mask(self, value):
        value |= self.x_as_zeros
        value &= self.x_as_ones

        return value
    
    def apply_address_mask(self, address):
        address |= self.x_as_ones
        addresses = []
        for floating_bits in product([ONE, ZERO], repeat=self.num_floating_bits):
            floater = int(self.template.format(*floating_bits), 2)
            floater &= address 
            addresses.append(floater)

        return addresses

def load(file):
    with open(file) as f:
        lines = [line.strip() for line in f.readlines()]

    return lines

def part1(instructions):
    mem = {}
    mask = Mask(EX * 36)

    for instruction in instructions:
        if (match := MASK_INSTRUCTION.match(instruction)) is not None:
            mask = Mask(match.group(1))
        elif (match :=MEM_INSTRUCTION.match(instruction)) is not None:
            address = int(match.group(1))
            value = int(match.group(2))
            mem[address] = mask.apply_value_mask(value)
        else:
            raise Exception(f'Unknown instruction: {instruction}')

    return sum(mem.values())

# I think there are some optimized solutions, but I'm done thinking about it and hope brute force is fast enough.
def part2(instructions):
    mem = {}
    mask = Mask(ZERO * 36)

    for instruction in instructions:
        if (match := MASK_INSTRUCTION.match(instruction)) is not None:
            mask = Mask(match.group(1))
        elif (match :=MEM_INSTRUCTION.match(instruction)) is not None:
            address_base = int(match.group(1))
            value = int(match.group(2))
            for address in mask.apply_address_mask(address_base):
                mem[address] = value
        else:
            raise Exception(f'Unknown instruction: {instruction}')

    return sum(mem.values())

def main():
    instructions = load('test1.txt')
    value = part1(instructions)
    print(f'Test 1 - Part 1: {value}')
    assert value == 165
    instructions = load('test2.txt')
    value = part2(instructions)
    print(f'Test 1 - Part 2: {value}')
    assert value == 208

    instructions = load('input.txt')
    value = part1(instructions)
    print(f'Part 1: {value}')
    value = part2(instructions)
    print(f'Part 2: {value}')

if __name__ == '__main__':
    main()