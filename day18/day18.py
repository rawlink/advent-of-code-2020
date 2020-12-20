#!/usr/bin/env python3
from collections import deque

ADD = '+'
MUL = '*'
LEFT = '('
RIGHT = ')'
SPACE = ' '

def load(file):
    with open(file) as f:
        exercises = [line.strip() for line in f.readlines()]
    
    return exercises

def operate(a, b, op):
    if op == ADD:
        return a + b
    elif op == MUL:
        return a * b
    else:
        raise Exception(f'Unknown operator: {op}')

def part1_op_precedence_gte(op1, op2):
    return True

def part2_op_precedence_gte(op1, op2):
    if op1 != op2 and op1 == MUL:
        return False

    return True

def part1(exercises):
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

# def part2(exercises):
#     total = 0

#     for exercise in exercises:
#         values = deque()
#         ops = deque()
#         for c in exercise:
#             if c == SPACE:
#                 continue
#             elif c.isdigit():
#                 num = int(c)
#                 if len(ops) > 1 and ops[-1] == ADD:
#                     values.append(operate(values.pop(), num, ops.pop()))
#                 else:
#                     values.append(num)
#             elif c == LEFT:
#                 ops.append(c)
#             elif c == RIGHT:
#                 while ops[-1] != LEFT:
#                     op = ops.pop()
#                     a = values.pop()
#                     b = values.pop()
#                     values.append(operate(a, b, op))
#                 ops.pop() # discard the left parentheses that should be left on the op stack
#                 if len(ops) > 0 and ops[-1] == ADD:
#                     values.append(operate(values.pop(), values.pop(), ops.pop()))
#             elif c == ADD or c == MUL:
#                 ops.append(c)
#             else:
#                 raise Exception('Should not have reached here')

#         while len(ops) > 0:
#             values.append(operate(values.pop(), values.pop(), ops.pop()))

#         if len(values) != 1:
#             raise Exception('Should not have reached here either')
        
#         total += values[0]

#     return total

def part2(exercises):
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
    exercises = load('test1.txt')
    value = part1(exercises)
    print(f'Test 1 - Part 1: {value}')
    assert value == 26335
    value = part2(exercises)
    print(f'Test 1 - Part 2: {value}')
    assert value == 693891

    exercises = load('input.txt')
    value = part1(exercises)
    print(f'Part 1: {value}')
    value = part2(exercises)
    print(f'Part 2: {value}')

if __name__ == '__main__':
    main()