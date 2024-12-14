# Day 14 Advent of Code
# Author: George Paraschiv
# Date: 2024-12-14

import time

# Parse Input
def parseInput():
    with open("input.txt", "r") as input:
        lines = input.readlines()
    
    return lines

# Q1 : 
def q1():

    input = parseInput()
    start = time.perf_counter()

    total = 0

    elapsed = (time.perf_counter() - start) * 1000000
    return total, round(elapsed)

# Q2 : 
def q2():

    input = parseInput()
    start = time.perf_counter()
    
    total = 0

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
