import csv
import re
from pprint import pprint

"""
Search day3_input for sequence mul(X,Y) where X and Y are integers
mul(X,Y) multiples the integers to get a result (X*Y)

Corrupted, similar sequences must be ignored:
    mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) etc

There are two new instructions you'll need to handle:

The do() instruction enables future mul instructions.
The don't() instruction disables future mul instructions.
Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

Given following string:

xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))=48

mul(1,1)mul[1,1]don't()mul(2,2)mul[2,2]do()mul(3,3)mul[3,3]don't()mul(4,4)mul[4,4]do()mul(5,5)mul[5,5]don't()mul(6,6)mul[6,6]do()mul(7,7)mul[7,7]=84

There are only TWO valid sequences:
    mul(2,4)
    mul(8,5)

Adding their results together gives the answer:
    161 (2*4 + 5*5 + 11*8 + 8*5)

Calculate the total from day3_input.csv
"""

def create_memory():

    txt_file = 'data/day3_input.txt'

    with open(txt_file, 'r') as file:
        corrupted_memory = ''.join(line.strip() for line in file)

    return corrupted_memory
    
def extract_valid_memory_string():

    corrupted_memory = create_memory()

    valid_memory_string = ""

    # To match numbers before first "don't()"
    first_section = re.match(r"^(.*?)don't\(\)", corrupted_memory)

    print(1, first_section.group(1))

    # To match strings between "do()" and "don't() OR "do()" and "do()"
    between_sections = re.findall(r"do\(\)(.*?)don't\(\)|do\(\)", corrupted_memory)

    print(2, between_sections)

    # To match numbers after final "do()"
    last_section = re.search(r'do\(\)([^do]*?)$', corrupted_memory)   

    print(3, last_section)

    if first_section:
        valid_memory_string += first_section.group(1)

    if between_sections:
        for item in between_sections:   
            valid_memory_string += item
    
    if last_section:
        valid_memory_string += last_section.group(1)

    return valid_memory_string

def extract_valid_muls():

    extract_mul_pattern = r'mul\(\d+,\d+\)'

    multipliers = ""

    valid_memory_strings = extract_valid_memory_string()

    valid_multipliers = re.findall(extract_mul_pattern, valid_memory_strings)

    for multiplier in valid_multipliers:

        multipliers += multiplier

    return multipliers

def calculate_total():
    
    total = 0

    valid_muls = extract_valid_muls()

    extract_digit_pattern = r'mul\((\d+),(\d+)\)'

    matches = re.findall(extract_digit_pattern, valid_muls)

    print(matches)

    pairs = [[int(a), int(b)] for a, b in matches]

    pprint(pairs)

    for pair in pairs:
        total += pair[0] * pair[1]

    print(total)
    return total

calculate_total()

# Numbers tried:
# 90650125 x
# 89829571 x
# 78147520 x
# 71639165 x