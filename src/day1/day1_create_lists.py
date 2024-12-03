import pandas as pd

def create_lists():
    # Create a dataframe from the input data
    df = pd.read_csv('data/day1/day1_input.csv', sep='\s+', header=None, names=['a', 'b'])

    # Create a list from each column of the dataframe
    a = df['a'].tolist()
    b = df['b'].tolist()

    return [a,b]