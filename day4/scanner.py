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

def merge_passport_data(passport, data):
    fields = data.split()
    for field in fields:
        [key,value] = field.split(':')
        passport[key] = value

def parse_passports(lines):
    passports = []
    passport = {}

    for line in lines:
        if not line:
            passports.append(passport)
            passport = {}
        else:
            merge_passport_data(passport, line)

    if passport:
        passports.append(passport)

    return passports


def is_valid_passport(passport):
    return BIRTH_YEAR in passport and \
        ISSUE_YEAR in passport and \
        EXPIRATION_YEAR in passport and \
        HEIGHT in passport and \
        HAIR_COLOR in passport and \
        EYE_COLOR in passport and \
        PASSPORT_ID in passport

def is_valid_year(year, min, max):
    valid = min <= year <= max

    return valid


def is_valid_height(height):
    pattern = re.compile('^(\\d+)(in|cm)$')
    match = pattern.match(height)

    if not match:
        return False

    val = int(match.group(1))
    unit = match.group(2)

    valid = False
    if unit == 'in':
        valid = val >= 59 and val <= 76
    elif unit == 'cm':
        valid = val >= 150 and val <= 193

    return valid

def is_valid_hair_color(color):
    pattern = re.compile('^#[\\da-f]{6}')
    valid = bool(pattern.match(color))

    return valid

def is_valid_eye_color(color):
    valid = color in VALID_EYE_COLORS

    return valid

def is_valid_passport_id(id):
    pattern = re.compile('^[\\d]{9}$')
    valid = bool(pattern.match(id))

    return valid

def is_valid_passport_v2(passport):
    if not (BIRTH_YEAR in passport and \
    ISSUE_YEAR in passport and \
    EXPIRATION_YEAR in passport and \
    HEIGHT in passport and \
    HAIR_COLOR in passport and \
    EYE_COLOR in passport and \
    PASSPORT_ID in passport):
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

def main():
    with open('test_passports.txt') as f:
        test_lines = [line.strip() for line in f.readlines()]

    with open('passports.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    test_passports = parse_passports(test_lines)
    passports = parse_passports(lines)

    valid_passports = [passport for passport in passports if is_valid_passport(passport)]
    valid_test_passports_v2 = [passport for passport in test_passports if is_valid_passport_v2(passport)]
    valid_passports_v2 = [passport for passport in passports if is_valid_passport_v2(passport)]

    print(f'Valid Passports: {len(valid_passports)}')
    print(f'Valid Test Passports V2(there should only be 8): {len(valid_test_passports_v2)}')
    print(f'Valid Passports V2: {len(valid_passports_v2)}')

if __name__ == '__main__':
    main()
