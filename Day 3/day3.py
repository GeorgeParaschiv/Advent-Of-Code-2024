# Day 3 Advent of Code
# Author: George Paraschiv
# Date: 2024-12-03

import re

# Q1 : O(n)
def q1(input):

    sum = 0

    matches = re.findall(r'mul\(([1-9]\d*),([1-9]\d*)\)', input)

    for match in matches:
        sum += int(match[0]) * int(match[1])

    return sum

# Q2 : O(n)
def q2(input):

    sum = 0

    # Find all occurences of do() or don't()
    matches = [(match.end(), 1 if match.group() == "do()" else 0) for match in re.finditer(r"do\(\)|don't\(\)", input)]

    # Find all do() don't() pairs including from start up to first don't()
    startIndex = 0
    endIndex = 0

    for match in matches:
        if match[1] == 0 and startIndex != -1:
            endIndex = match[0]
            sum += q1(input[startIndex:endIndex])
            startIndex = -1
        elif match[1] == 1 and startIndex == -1:
            startIndex = match[0]

    # Find all occurences after do() after last don't()
    if startIndex != -1:
        sum += q1(input[startIndex:])        

    return sum

# ---------- Main ----------
if __name__ == "__main__":

    # Parse Input
    with open("input.txt", "r") as input:
        lines = ''.join([line.rstrip() for line in input.readlines()])

    print(f"Total sum of matches is: {q1(lines)}")
    print(f"Total sum of matches is: {q2(lines)}")