#!/usr/bin/env python3
import re

BIRTH_YEAR='byr'
ISSUE_YEAR='iyr'
EXPIRATION_YEAR='eyr'
HEIGHT='hgt'
HAIR_COLOR='hcl'
EYE_COLOR='ecl'
PASSPORT_ID='pid'
COUNTRY_ID='cid'

VALID_EYE_COLORS = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def parse(raw_passport):
    return { k:v for k,v in (kv.split(':') for kv in raw_passport) }

def load(file):
    with open(file) as f:
        raw_passports = [line.strip().split() for line in f.read().split('\n\n')]

    return [parse(raw_passport) for raw_passport in raw_passports]

def is_valid_passport(passport):
    return BIRTH_YEAR in passport and \
        ISSUE_YEAR in passport and \
        EXPIRATION_YEAR in passport and \
        HEIGHT in passport and \
        HAIR_COLOR in passport and \
        EYE_COLOR in passport and \
        PASSPORT_ID in passport

def is_valid_year(year, min, max):
    return min <= year <= max

def is_valid_height(height):
    pattern = re.compile('^(\\d+)(in|cm)$')
    match = pattern.match(height)

    if not match:
        return False

    val = int(match.group(1))
    unit = match.group(2)

    valid = False
    if unit == 'in':
        return 59 <= val <= 76
    elif unit == 'cm':
        return 150 <= val <= 193

    return False

def is_valid_hair_color(color):
    pattern = re.compile('^#[\\da-f]{6}')
    return bool(pattern.match(color))

def is_valid_eye_color(color):
    return color in VALID_EYE_COLORS

def is_valid_passport_id(id):
    pattern = re.compile('^[\\d]{9}$')
    return bool(pattern.match(id))

def is_valid_passport_v2(passport):
    if not is_valid_passport(passport):
        return False

    birth_year = int(passport[BIRTH_YEAR])
    issuer_year = int(passport[ISSUE_YEAR])
    expiration_year = int(passport[EXPIRATION_YEAR])
    height = passport[HEIGHT]
    hair_color = passport[HAIR_COLOR]
    eye_color = passport[EYE_COLOR]
    passport_id = passport[PASSPORT_ID]

    valid = is_valid_year(birth_year, 1920, 2002) and \
        is_valid_year(issuer_year, 2010, 2020) and \
        is_valid_year(expiration_year, 2020, 2030) and \
        is_valid_height(height) and \
        is_valid_hair_color(hair_color) and \
        is_valid_eye_color(eye_color) and \
        is_valid_passport_id(passport_id)

    return valid

def part1(passports):
    '''
    >>> part1(load('test0.txt'))
    23
    >>> part1(load('test1.txt'))
    2
    '''
    return len(list(passport for passport in passports if is_valid_passport(passport)))

def part2(passports):
    '''
    >>> part2(load('test2.txt'))
    4
    '''
    return len(list(passport for passport in passports if is_valid_passport_v2(passport)))
    

def main():
    passports = load('input.txt')
    value = part1(passports)
    print(f'Part 1: {value}')
    assert value == 219

    value = part2(passports)
    print(f'Part 2: {value}')
    assert value == 127

if __name__ == '__main__':
    main()