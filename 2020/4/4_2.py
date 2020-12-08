# coding: utf-8
import doctest
import math
import itertools
from collections import Counter
import re


def has_all_fields(fs):
    return len(fs) == 8 or (len(fs) == 7 and 'cid' not in fs)

def is_valid(fs):
    '''
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    '''

    try:
        valid = True
        valid &= 1920 <= int(fs['byr']) <= 2002
        valid &= 2010 <= int(fs['iyr']) <= 2020
        valid &= 2020 <= int(fs['eyr']) <= 2030
        valid &= height(fs['hgt'])
        valid &= bool(re.match('^#[0-9a-f]{6}$', fs['hcl']))
        valid &= bool(re.match('^(amb|blu|brn|gry|grn|hzl|oth)$', fs['ecl']))
        valid &= bool(re.match('^\d{9}$', fs['pid']))
        return valid
    except Exception as e:
        return False


def height(h):
    '''
       hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.

    '''
    m = re.search('^(\d+)(cm|in)$', h)
    if not m:
        return False
    num, unit = m.groups()
    if unit == 'cm':
        return 150 <= int(num) <= 193
    else:
        return 59 <= int(num) <= 76


count = 0
for p in open('input.txt').read().split('\n\n'):
    fs = {p.split(':')[0]: p.split(':')[1] for p in p.replace('\n', ' ').split(' ') if ':' in p}
    print(fs)

    if has_all_fields(fs) and is_valid(fs):
        print(fs, 'valid')
        count += 1

print(count)


# for line in open('input.test').readlines():
#     print(re.search("(\d+)-(\d+) (\w): (\w+)", line).groups())

# if __name__ == "__main__":
#     doctest.testmod()