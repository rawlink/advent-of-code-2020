#!/usr/bin/env python3
from collections import deque

ADD = '+'
MUL = '*'
LEFT = '('
RIGHT = ')'
SPACE = ' '

def load(file):
    with open(file) as f:
        return [line.strip() for line in f.readlines()]

def operate(a, b, op):
    if op == ADD:
        return a + b
    elif op == MUL:
        return a * b
    else:
        raise Exception(f'Unknown operator: {op}')

def part1(exercises):
    '''
    >>> part1(load('test1.txt'))
    26335
    '''
    total = 0
    # Seeing as the input data only has single digit numbers, I'm going to take advantage of that. I'm also taking advantage
    # of the fact that the input is "correct".
    for exercise in exercises:
        stack = deque()
        subtotal = 0
        op = ADD
        for c in exercise:
            if c == SPACE:
                continue
            elif c == LEFT:
                stack.append((subtotal, op))
                subtotal = 0
                op = ADD
            elif c == RIGHT:
                (prev,op) = stack.pop()
                subtotal = operate(prev, subtotal, op)
            elif c == ADD or c == MUL:
                op = c
            elif c.isdigit():
                num = int(c)
                subtotal = operate(subtotal, num, op)
            else:
                raise Exception('Should not have reached here')

        total += subtotal
    return total

def part2(exercises):
    '''
    >>> part2(load('test1.txt'))
    693891

    '''
    # Had to look up shunting algorithm for a reminder on how it should work.
    total = 0

    for exercise in exercises:
        values = deque()
        ops = deque()
        for c in exercise:
            if c == SPACE:
                continue
            elif c.isdigit():
                values.append(int(c))
            elif c == LEFT:
                ops.append(c)
            elif c == RIGHT:
                while ops[-1] != LEFT:
                    values.append(operate(values.pop(), values.pop(), ops.pop()))
                ops.pop() # discard the left parentheses that should be left on the op stack
            elif c == ADD or c == MUL:
                while len(ops) > 0 and ops[-1] != LEFT and not (ops[-1] != c and ops[-1] == MUL):
                    values.append(operate(values.pop(), values.pop(), ops.pop()))
                ops.append(c)
            else:
                raise Exception('Should not have reached here')

        while len(ops) > 0:
            values.append(operate(values.pop(), values.pop(), ops.pop()))

        if len(values) != 1:
            raise Exception('Should not have reached here either')
        
        total += values[0]

    return total


def main():
    exercises = load('input.txt')
    value = part1(exercises)
    print(f'Part 1: {value}')
    assert value == 12918250417632

    value = part2(exercises)
    print(f'Part 2: {value}')
    assert value == 171259538712010

if __name__ == '__main__':
    main()