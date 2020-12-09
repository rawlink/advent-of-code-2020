#!/usr/bin/env python3
CODE_FRONT = 'F'
CODE_BACK = 'B'
CODE_LEFT = 'L'
CODE_RIGHT = 'R'

MAX_ROWS = 128
MAX_COLS = 8

def convert_binary(binary):
    return int(binary, 2)

def get_row(row_code):
    row_code = row_code.replace(CODE_FRONT, '0')
    row_code = row_code.replace(CODE_BACK, '1')

    return convert_binary(row_code)

def get_col(col_code):
    col_code = col_code.replace(CODE_LEFT, '0')
    col_code = col_code.replace(CODE_RIGHT, '1')

    return convert_binary(col_code)

def convert_to_binary(num, digits):
    return f'{num:08b}'[-digits:]

def get_row_code(num):
    row_code = convert_to_binary(num, 7).replace('0', CODE_FRONT)
    return row_code.replace('1', CODE_BACK)

def get_col_code(num):
    col_code = convert_to_binary(num, 3).replace('0', CODE_LEFT)
    return col_code.replace('1', CODE_RIGHT)

def get_seat_id(row, col):
    return (row * 8) + col

def main():
    with open('boarding_passes.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    max_row = 0
    max_col = 0
    max_seat_id = 0

    seat_candidates = [[True for row_num in range(MAX_COLS)] for col_num in range(MAX_ROWS)]

    for line in lines:
        if len(line) != 10:
            print('Bad input')
            exit(1)

        row_code = line[:7]
        col_code = line[-3:]

        row = get_row(row_code)
        col = get_col(col_code)
        seat_id = get_seat_id(row, col)

        if row > max_row:
            max_row = row

        if col > max_col:
            max_col = col


        if seat_id > max_seat_id:
            max_seat_id = seat_id

        if seat_candidates[row][col] == True:
            seat_candidates[row][col] = False
        else:
            print("Duplicate seating assignments?")
            exit(1)
    
    for row_num in range(max_row + 1):
       for col_num in range(max_col + 1):
           if seat_candidates[row_num][col_num]:
               print(f'CANDIDATE: Row: {row_num}, Col: {col_num}, Code: {get_row_code(row_num)}{get_col_code(col_num)}, Seat ID: {get_seat_id(row_num, col_num)}')

    print(f'Max row: {max_row}')
    print(f'Max col: {max_col}')
    print(f'Max seat ID: {max_seat_id}')

if __name__ == '__main__':
    main()
