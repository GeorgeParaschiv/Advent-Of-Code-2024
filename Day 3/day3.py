# Day 3 Advent of Code
# Author: George Paraschiv
# Date: 2024-12-03

import re

# Parse Input
def parseInput():
    with open("input.txt", "r") as input:
        lines = ''.join([line.rstrip() for line in input.readlines()])
    
    return lines

# Function to find multiplication statements in a string
def findMul(string):
    matches = re.findall(r'mul\(([1-9]\d*),([1-9]\d*)\)', string)

    sum = 0
    for match in matches:
        sum += int(match[0]) * int(match[1])
        
    return sum

# Q1 : O(n)
def q1():

    input = parseInput()  
    
    return findMul(input)

# Q2 : O(n)
def q2():

    # Find all occurences of do() or don't()
    input = parseInput()
    matches = [(match.end(), 1 if match.group() == "do()" else 0) for match in re.finditer(r"do\(\)|don't\(\)", input)]

    # Find all do() don't() pairs including from start up to first don't()
    sum = 0
    startIndex = 0
    endIndex = 0

    for match in matches:
        if match[1] == 0 and startIndex != -1:
            endIndex = match[0]
            sum += findMul(input[startIndex:endIndex])
            startIndex = -1
        elif match[1] == 1 and startIndex == -1:
            startIndex = match[0]

    # Find all occurences after do() after last don't()
    if startIndex != -1:
        sum += findMul(input[startIndex:])        

    return sum

# ---------- Main ----------
if __name__ == "__main__":

    print(f"Multiplication Sum: {q1()}")
    print(f"Enabled Multiplication Sum: {q2()}")