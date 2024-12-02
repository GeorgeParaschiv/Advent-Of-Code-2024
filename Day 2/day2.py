import math

# O(k)
def isSafe(report):

    ascending = report[1] - report[0]
    
    if ascending == 0: 
        return 0

    if (ascending < 0):
        return all(((report[i+1] < report[i]) and (report[i+1] > report[i] - 4)) for i in range(len(report) - 1))
    else:
        return all(((report[i+1] > report[i]) and (report[i+1] < report[i] + 4)) for i in range(len(report) - 1))
    
# O(k)
def isSafeDampened(report):

    if isSafe(report):
        return 1

    ascending = report[1] - report[0]
    
    if ascending == 0: 
        return 0

    if (ascending < 0):
        for i in range(len(report) - 1):
        return all(((report[i+1] < report[i]) and (report[i+1] > report[i] - 4)) for i in range(len(report) - 1))
    else:
        return all(((report[i+1] > report[i]) and (report[i+1] < report[i] + 4)) for i in range(len(report) - 1))
        
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
        safe += isSafe(report)

    print(f"Total Safe Reports is: {safe}")

# Main
if __name__ == "__main__":

    reports = []

    # Parse input into two lists
    with open("input.txt", "r") as input:
        reports = [[int(level) for level in line.rstrip(" ").split()] for line in input]

    q1(reports)
    #q2(reports)