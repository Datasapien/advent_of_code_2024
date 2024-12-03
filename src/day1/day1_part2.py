import pandas as pd

"""
# Take two lists, a and b:
    a = [3,4,2,1,3,3]
    b = [4,3,5,3,9,3]
# Find out how many times each number in 'a' appears in 'b'
# Multiply a[i] by its frequency in b to find a 'similarity score':
    a[0] = 3
    3 appears in b 3 times; score = 3*3 = 9
    a[1] = 4
    4 appears in b 1 time; score = 4*1 = 4
    ...
    Total similarity score = 31
"""

def create_lists():
# Create a dataframe from the input data
    df = pd.read_csv('data/day1/day1_input.csv', sep='\s+', header=None, names=['a', 'b'])

    # Create a list from each column of the dataframe
    a = df['a'].tolist()
    b = df['b'].tolist()

    # Sort the lists and pass them to find_distance()
    a.sort()
    b.sort()

    return [a,b]

def similarity_score():
    
    return 0