#!/usr/bin/env python3
import re

ACC = 'acc'
JMP = 'jmp'
NOP = 'nop'

def parse_instruction(line):
    pattern = re.compile('^(\w+) ([+|-]\d+)$')
    match = pattern.match(line)
    return (match.group(1), int(match.group(2)))

def compile_code(sources):
    code = []
    for line in sources:
        code.append(parse_instruction(line))
    return code

def eval_instruction(instruction, fix):
    (op, value) = instruction

    if op == ACC:
        return (1,value)
    
    if op == JMP:
        return (value if not fix else 1, 0)

    if op == NOP:
        return (1 if not fix else value, 0)

    raise Exception(f'Unknown instruction: {instruction}')

def run_code(code, fix):
    acc = 0
    visited = set()
    pos = 0
    done = len(code)

    saved_pos = 0
    saved_acc = 0
    saved_visited = set()

    while True:
        if pos == done:
            return acc

        if pos in visited:
            if not fix:
                print('Loop detected')
                return acc
            else:
                (pos_delta, acc_delta) = eval_instruction(code[saved_pos], False)
                saved_pos += pos_delta
                saved_acc += acc_delta

                pos = saved_pos
                acc = saved_acc
                visited = saved_visited
                continue

        visited.add(pos)

        if pos == saved_pos and fix:
            saved_visited = visited.copy()
            saved_acc = acc

        (pos_delta, acc_delta) = eval_instruction(code[pos], pos == saved_pos and fix)
        pos += pos_delta
        acc += acc_delta


def main():
    with open('boot.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    
    code = compile_code(lines)

    acc = run_code(code, False)
    print(f'Accumulator without fix: {acc}')

    acc = run_code(code, True)
    print(f'Accumulator with fix: {acc}')

if __name__ == '__main__':
    main()
