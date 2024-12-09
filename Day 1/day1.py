# Day 1 Advent of Code
# Author: George Paraschiv
# Date: 2024-12-01

import time

# Parse Input
def parseInput():
    
    with open("input.txt", "r") as input:
        lines = [line.rstrip().split() for line in input.readlines()]
        
    list1 = [int(line[0]) for line in lines]
    list2 = [int(line[1]) for line in lines]
    
    return list1, list2

# Q1 : O(n * logn)
def q1():
    
    list1, list2 = parseInput()
    start = time.perf_counter()
    
    list1.sort()
    list2.sort()

    total = 0
    for index, line in enumerate(list1):
        total += abs(list1[index]-list2[index])
        
    elapsed = (time.perf_counter() - start) * 1000000
    return total, round(elapsed) 

# Q2 : O(n)
def q2():
    
    list1, list2 = parseInput()  
    start = time.perf_counter()

    # Create hashmap of list2: key = id, value = # of times id appears in list2
    dict2 = {}
    for id in list2:
        if id in dict2:
            dict2[id] += 1
        else:
            dict2[id] = 1

    # Check if item in list 1 is in hashmap and update similarity score
    total = 0
    for id in list1:
        if id in dict2:
            total += id * dict2[id]

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