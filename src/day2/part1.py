"""
Input data consists of 'reports' (rows) and 'levels' (columns)
Following data consists of 6 reports and 5 levels:

    7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9

Reports can either be SAFE or UNSAFE - we want to track SAFE reports only
SAFE reports either:

    - numbers ALL increase OR decrease;
    - any two adjacent levels differ by at least 1 and at most 3;

    7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
    1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
    9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
    1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
    8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
    1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

Need to output the number of SAFE reports
"""

def create_reports():

    csv_file = "data/day2_input.csv"

    with open(csv_file, 'r') as file:
        rows = [list(map(int, line.strip().split())) for line in file]

    return rows


def safe_reports():

    reports = create_reports()

    safe_count = 0

    for report in reports:

        is_increasing = all(report[i] <= report[i + 1] for i in range(len(report) - 1))
        is_decreasing = all(report[i] >= report[i + 1] for i in range(len(report) - 1))
        valid_differences = all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))

        if (is_increasing or is_decreasing) and valid_differences:
            safe_count += 1

    print(safe_count)

    return safe_count

safe_reports()