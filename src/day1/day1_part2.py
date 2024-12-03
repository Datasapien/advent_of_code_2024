from day1_create_lists import create_lists

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

def similarity_score():

    create_lists()
    
    return 0

# Only call the function if this file is executed directly
if __name__ == "__main__":
    similarity_score()