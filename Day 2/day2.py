# Day 2 Advent of Code
# Author: George Paraschiv
# Date: 2024-12-02

import time

# Parse Input
def parseInput():
    with open("input.txt", "r") as input:
        reports = [[int(level) for level in line.rstrip(" ").split()] for line in input]
    
    return reports

# Function to check if a report is safe
def isSafe(report):
 
    sign = 1 if report[1] - report[0] > 0 else -1

    return all(((sign*report[i+1] > sign*report[i]) and (sign*report[i+1] < sign*report[i] + 4)) for i in range(len(report) - 1))

# Function to check if a dampened report is safe    
def isSafeDampened(report):

    if isSafe(report[1:]):
        return True

    sign = 1 if report[1] - report[0] > 0 else -1
    
    for i in range(len(report) - 1):
        if ((sign*report[i+1] <= sign*report[i]) or (sign*report[i+1] > sign*report[i] + 3)):
            return (isSafe(report[:i] + report[i+1:]) or isSafe(report[:i+1] + report[i+2:]))

# Q1 : O(n)
def q1():

    reports = parseInput()  
    start = time.perf_counter()
    
    total = 0
    for report in reports:
        total += isSafe(report)

    elapsed = (time.perf_counter() - start) * 1000000
    return total, round(elapsed) 

# Q2 : O(n)
def q2():
    
    reports = parseInput()
    start = time.perf_counter()

    total = 0
    for report in reports:
        total += isSafeDampened(report)

    elapsed = (time.perf_counter() - start) * 1000000
    return total, round(elapsed) 

# ---------- Main ----------
if __name__ == "__main__":

    sol1, time1 = q1()
    print(f"Part 1 Solution: {sol1}")
    print(f"Part 1 Time: {time1} us") 
    
    sol2, time2 = q2()
    print(f"Part 2 Solution: {sol2}")
    print(f"Part 2 Time: {time2} us") 