#!/usr/bin/env python3
def parse(instruction):
    return (instruction[0], int(instruction[1:]))

def load(file):
    with open(file) as f:
        instructions = [parse(line.strip()) for line in f.readlines()]
    return instructions

def main():
    instructions = load('test1.txt')
    print(instructions)

    instructions = load('input.txt')
    print(instructions)

if __name__ == '__main__':
    main()