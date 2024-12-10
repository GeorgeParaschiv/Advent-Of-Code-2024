# Day 9 Advent of Code
# Author: George Paraschiv
# Date: 2024-12-09

import time
from collections import deque, defaultdict

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
            diskMap += [-1] * num
        else:
            diskMap += [ID] * num
            ID += 1
    
    return len(diskMap), diskMap

# Q1 : O(n)
def q1():

    input = parseInput()
    start = time.perf_counter()
        
    diskSize, diskMap = createDiskMap(input)
            
    # Compact the Disk
    startIndex = 0
    finishIndex = diskSize - 1
        
    while(startIndex < finishIndex):
        if (diskMap[startIndex] == -1):
            if (diskMap[finishIndex] == -1):
                finishIndex -= 1
            else:
                diskMap[startIndex], diskMap[finishIndex] = diskMap[finishIndex], diskMap[startIndex]    
        else:
            startIndex += 1
    
    # Compute Checksum
    total = 0
            
    for index in range(diskSize):
        if diskMap[index] != -1:
            total += diskMap[index] * index
    
    elapsed = (time.perf_counter() - start) * 1000000
    return total, round(elapsed)

# Function to find the length of ID blocks
def findLength(diskMap, index):
    
    ID = diskMap[index]
    length = 0
    
    while(diskMap[index] == ID):
        index -= 1
        length += 1
    
    return index, length 
  
# Q2 : O(n^2)
def q2():

    input = parseInput()
    start = time.perf_counter()
    
    diskSize, diskMap = createDiskMap(input)
    
    # Compact the Disk
    finishIndex = diskSize - 1
    
    # Create Free Space Hash
    freeSpace = {}
    spaces = 0
    
    for i in range(diskSize):
        if (diskMap[i] == -1):
            startIndex = i
            spaces += 1
        elif (spaces != 0):
            freeSpace.update({(startIndex - spaces):spaces})
            spaces = 0   
        
    while(freeSpace):
        
        if diskMap[finishIndex] == -1:
            finishIndex -= 1
            freeSpace.pop(finishIndex, None)
        else:
            
            finishIndex, length = findLength(diskMap, finishIndex)  
            
            for keyIndex, key in enumerate(freeSpace.keys()):
                if (freeSpace[key] >= length):
                    diskMap[key + 1 : key + length + 1], diskMap[finishIndex + 1 : finishIndex + length + 1] = diskMap[finishIndex + 1 : finishIndex + length + 1], diskMap[key + 1 : key + length + 1]
                    
                    if (freeSpace[key] > length):
                        items = list(freeSpace.items())
                        items.insert(keyIndex, ((key+length),(freeSpace[key]-length)))
                        freeSpace = dict(items)
                        
                    del freeSpace[key] 
                    break
            
    # Compute Checksum
    total = 0
            
    for index in range(diskSize):
        if diskMap[index] != -1:
            total += diskMap[index] * index
    
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
