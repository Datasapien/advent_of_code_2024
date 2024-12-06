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

xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))

There are only TWO valid sequences:
    mul(2,4)
    mul(8,5)

Adding their results together gives the answer:
    161 (2*4 + 5*5 + 11*8 + 8*5)

Calculate the total from day3_input.csv
"""

def create_memory():

    csv_file = 'data/day3_input.csv'

    with open(csv_file, 'r') as file:
        string = csv.reader(file, delimiter = ' ')

        corrupted_memory = ""

        for row in string:
                   
            for item in row:
                corrupted_memory += f'{item}'

    pprint(corrupted_memory)
    return corrupted_memory
    
def extract_valid_memory_strings():

    corrupted_memory = create_memory()

    valid_memory_strings = []

    for memory_string in corrupted_memory:

        # Pattern to match numbers before first "don't()"
        first_section = re.match(r'^(.*?)don\'t\(\)', memory_string)
        
        # Pattern to match numbers between "do()" and "don't()"
        between_sections = re.findall(r'do\(\)(.*?)don\'t\(\)', memory_string)
        
        # Pattern to match numbers after final "do()"
        last_section = re.search(r'do\(\)([^\']+)$', memory_string)    

        if first_section:
            valid_memory_strings.append(first_section.group(1))

        if between_sections:     
            valid_memory_strings.extend(between_sections)
        
        if last_section:
            valid_memory_strings.append(last_section.group(1)) 

    return(valid_memory_strings)

def extract_valid_muls():

    extract_mul_pattern = r'mul\(\d+,\d+\)'

    multipliers = []

    valid_memory_strings = extract_valid_memory_strings()

    for valid_memory_string in valid_memory_strings:

        multipliers.extend(re.findall(extract_mul_pattern, valid_memory_string))

    return multipliers

def calculate_total():
    
    total = 0

    valid_muls = extract_valid_muls()

    extract_digit_pattern = r'mul\((\d+),(\d+)\)'

    for mul in valid_muls:

        digits = re.match(extract_digit_pattern, mul)

        total += int(digits.group(1)) * int(digits.group(2))

    print(total)
    return total

calculate_total()


