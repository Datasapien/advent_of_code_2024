import pandas as pd

"""
Take two lists, a and b:
    a = [3,4,2,1,3,3]
    b = [4,3,5,3,9,3]
air up the numbers and find out how far apart they each are
    sorted_a = [1,2,3,3,3,4]
    sorted_b = [3,3,3,4,5,9]
    distance = [2,1,0,1,2,5] = 11
Real input comes from .txt file with two columns of 5 digit numbers separated by 3 whitespaces
"""

def create_lists():
    df = pd.read_csv('data/day1_input.csv', sep='\s+', header=None, names=['a', 'b'])

    a = df['a'].tolist()
    b = df['b'].tolist()

    return [a,b]

def find_distance():
    
    lists = create_lists()

    a = lists[0]
    b = lists[1]

    a.sort()
    b.sort()

    distance = 0

    for i in range(len(a)):

        distance += max(a[i] - b[i], b[i] - a[i])

    print(distance)
    return distance


find_distance()