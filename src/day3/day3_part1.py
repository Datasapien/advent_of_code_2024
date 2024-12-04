from pprint import pprint
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

    # Read day3_input.csv and output it

    csv_file = 'data/test_input.csv'

    with open(csv_file, 'r') as file:
        string = csv.reader(file, delimiter = ' ')

        corrupted_memory = []

        for row in string:
            
            for item in row:
                corrupted_memory.append(item)

        print(corrupted_memory)        
        return corrupted_memory
    
def multiplier_adder():
    
    total = 0

    corrupted_memory = create_memory()

    print(1, corrupted_memory)

    pattern = r'mul\(\d+,\d+\)'

    for memory_string in corrupted_memory:

        print(2, memory_string)

        multipliers = re.findall(pattern, memory_string)
        print(3, multipliers)

        for multiplier in multipliers:
            print(4, multiplier)

            pattern = r'mul\((\d+),(\d+)\)'

            digits = re.match(pattern, multiplier).groups()

            # print(digits)

            total += int(digits[0]) * int(digits[1])

    print(total)
    return total

create_memory()