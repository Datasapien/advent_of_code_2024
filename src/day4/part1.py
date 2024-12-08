import csv
from pprint import pprint

"""
Given a word search, find how many times a word appears! Up, Down, Left, Right, Diagonally. Letters CAN overlap.

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX

"XMAS" appears 18 times.
"""

def create_word_search():

    input_file = 'data/test_input.txt'

    with open(input_file, 'r') as file:
        string = csv.reader(file, delimiter = ' ')

        word_search = []

        for row in string:
            
            for item in row:

                word_search.append(list(item))

        pprint(word_search)
        return word_search
    
def find_X():

    word_search = create_word_search()

    num_rows = len(word_search)
    num_cols = len(word_search[0])

    print(num_rows)
    print(num_cols)
    
find_X()