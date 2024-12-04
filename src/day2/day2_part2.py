"""
Same rules as part1 apply, but an additional rule is created:

If a report would be deemed UNSAFE due to a SINGLE digit, it is deemed to be SAFE

7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
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
        is_safe = False

        is_increasing = all(report[i] <= report[i + 1] for i in range(len(report) - 1))
        is_decreasing = all(report[i] >= report[i + 1] for i in range(len(report) - 1))
        valid_differences = all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))

        if (is_increasing or is_decreasing) and valid_differences:
            is_safe = True


        # If it's not already safe, try removing levels one at a time:
        if not is_safe:  
            for i in range(len(report)):
                report_copy = report.copy()
                report_copy.pop(i)

                is_increasing = all(report_copy[j] <= report_copy[j + 1] for j in range(len(report_copy) - 1))
                is_decreasing = all(report_copy[j] >= report_copy[j + 1] for j in range(len(report_copy) - 1))
                valid_differences = all(1 <= abs(report_copy[j] - report_copy[j + 1]) <= 3 for j in range(len(report_copy) - 1))

                if (is_increasing or is_decreasing) and valid_differences:
                    is_safe = True
                    break

        if is_safe:
            safe_count += 1

    print(safe_count)
    return safe_count

safe_reports()