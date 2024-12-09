# Day 9 Advent of Code
# Author: George Paraschiv
# Date: 2024-12-09

import time, cProfile

# Parse Input
def parseInput():
    with open("input.txt", "r") as input:
        line = list(int(num) for num in input.readline().rstrip())   

    return line

# Function to create the diskMap
def createDiskMap(input):
    
    ID = 0
    diskMap = []
    
    # Create Disk Map
    for index, num in enumerate(input):
        if index % 2:
            diskMap += ["."] * num   
        else:
            diskMap += [str(ID)] * num
            ID += 1
    
    return diskMap

# Q1 : O(n)
def q1():

    input = parseInput()
    start = time.perf_counter()
        
    diskMap = createDiskMap(input)
            
    # Compact the Disk
    startIndex = 0
    finishIndex = len(diskMap) - 1
        
    while(startIndex < finishIndex):
        if (diskMap[startIndex] == "."):
            if (diskMap[finishIndex] == "."):
                finishIndex -= 1
            else:
                diskMap[startIndex], diskMap[finishIndex] = diskMap[finishIndex], diskMap[startIndex]    
        else:
            startIndex += 1
    
    # Compute Checksum
    total = 0
            
    for index, item in enumerate(diskMap):
        if item != ".":
            total += int(item) * index
    
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
