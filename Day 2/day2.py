# Day 2 Advent of Code

# O(k)
def isSafe(report):
 
    if len(set(report)) != len(report):
        return False

    sign = 1 if report[1] - report[0] > 0 else -1

    return all(((sign*report[i+1] > sign*report[i]) and (sign*report[i+1] < sign*report[i] + 4)) for i in range(len(report) - 1))
    
# O(k)
def isSafeDampened(report):

    if isSafe(report) or isSafe(report[1:]):
        return True

    sign = 1 if report[1] - report[0] > 0 else -1
    
    for i in range(len(report) - 1):
        if ((sign*report[i+1] <= sign*report[i]) or (sign*report[i+1] > sign*report[i] + 3)):
            return (isSafe(report[:i] + report[i+1:]) or isSafe(report[:i+1] + report[i+2:]))

# Q1 : O(kn)
def q1(reports):

    safe = 0
    for report in reports:
        safe += isSafe(report)

    print(f"Total Safe Reports is: {safe}")

# Q2 : O(kn)
def q2(reports):

    safe = 0
    for report in reports:
        safe += isSafeDampened(report)

    print(f"Total Safe Reports is: {safe}")

# Main
if __name__ == "__main__":

    reports = []

    # Parse input into two lists
    with open("input.txt", "r") as input:
        reports = [[int(level) for level in line.rstrip(" ").split()] for line in input]

    q1(reports)
    q2(reports)