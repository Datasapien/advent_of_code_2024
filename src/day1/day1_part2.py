import pandas as pd

"""
Take two lists, a and b:
    a = [3,4,2,1,3,3]
    b = [4,3,5,3,9,3]
Find out how many times each number in 'a' appears in 'b'
Multiply a[i] by its frequency in b to find a 'similarity score':
    a[0] = 3
    3 appears in b 3 times; score = 3*3 = 9
    a[1] = 4
    4 appears in b 1 time; score = 4*1 = 4
    ...
    Total similarity score = 31
"""
def create_lists():
    df = pd.read_csv('data/day1_input.csv', sep='\s+', header=None, names=['a', 'b'])

    a = df['a'].tolist()
    b = df['b'].tolist()

    return [a,b]

def similarity_score():

    lists = create_lists()

    a = lists[0]
    b = lists[1]

    score_dict = {}    

    for num in a:
        if num in b:
            score_dict.setdefault(num,0)
            score_dict[num] += b.count(num)

    score = 0

    for key, value in score_dict.items():
        score += key * value

    print(score)
    return score

similarity_score()