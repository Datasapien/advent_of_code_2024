"""
# Input data consists of 'reports' (rows) and 'levels' (columns)
# Following data consists of 6 reports and 5 levels:

    7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9

# Reports can either be SAFE or UNSAFE - we want to track SAFE reports only
# SAFE reports either:

    - numbers ALL increase OR decrease;
    - any two adjacent levels differ by at least 1 and at most 3;

    7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
    1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
    9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
    1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
    8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
    1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

# Need to output the number of SAFE reports
"""

def safe_reports():    

    return 0

# Only call the function if this file is executed directly
if __name__ == "__main__":
    safe_reports()