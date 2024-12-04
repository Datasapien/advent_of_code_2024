import csv
import re

"""
Search day3_input for sequence mul(X,Y) where X and Y are integers
mul(X,Y) multiples the integers to get a result (X*Y)

Corrupted, similar sequences must be ignored:
    mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) etc

Given following string:

    xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

There are only 4 valid sequences:
    mul(2,4)
    mul(5,5)
    mul(11,8)
    mul(8,5)

Adding their results together gives the answer:
    161 (2*4 + 5*5 + 11*8 + 8*5)

Calculate the total from day3_input.csv
"""

def create_memory():

    csv_file = 'data/day3_input.csv'

    with open(csv_file, 'r') as file:
        string = csv.reader(file, delimiter = ' ')

        corrupted_memory = []

        for row in string:
            
            for item in row:
                corrupted_memory.append(item)

        return corrupted_memory
    
def multiplier_adder():
    
    total = 0

    corrupted_memory = create_memory()

    extract_mul_pattern = r'mul\(\d+,\d+\)'

    for memory_string in corrupted_memory:

        multipliers = re.findall(extract_mul_pattern, memory_string)

        for multiplier in multipliers:

            extract_digit_pattern = r'mul\((\d+),(\d+)\)'

            digits = re.match(extract_digit_pattern, multiplier)

            total += int(digits.group(1)) * int(digits.group(2))

    print(total)
    return total

multiplier_adder()