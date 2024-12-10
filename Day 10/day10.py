# Day 10 Advent of Code
# Author: George Paraschiv
# Date: 2024-12-10

import time
from collections import defaultdict

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# Parse Input
def parseInput():
    with open("input.txt", "r") as input:
        lines = [[int(x) for x in list(line.rstrip())] for line in input.readlines()]
    
    return lines

def search(jumpSet, current):
    
    visited = {}
    for j in jumpSet.keys():
        visited[j] = 0

    queue = []
    
    queue.append(current)
    visited[current] = 1
    
    found = []
    while(queue):
        
        node = queue.pop()
        
        if node[0] == 9:
            found.append(node)
            visited[current] = 1
            
        for newNode in jumpSet[node]:
            if visited[newNode] != 1:
                queue.append(newNode)
                visited[newNode] = 1
             
    return found

# Q1 : 
def q1():

    grid = parseInput()
    start = time.perf_counter()
    
    jumps = defaultdict(list)
    maxRow = len(grid)
    maxCol = len(grid[0])
    
    # Create hash of possible movements
    for rowIndex in range(maxRow):
        for colIndex in range(maxCol):
            for dx, dy in DIRECTIONS:
                nx = rowIndex + dx
                ny = colIndex + dy
                if (0 <= nx < maxRow and 0 <= ny < maxCol and grid[nx][ny] == grid[rowIndex][colIndex] + 1):
                    jumps[(grid[rowIndex][colIndex], rowIndex, colIndex)].append((grid[nx][ny], rowIndex + dx, colIndex + dy))
                else:
                    jumps[(grid[rowIndex][colIndex], rowIndex, colIndex)]
    
    total = 0  
    for j in jumps.keys():
        if j[0] == 0:
            total += len(search(jumps, j)) 

    elapsed = (time.perf_counter() - start) * 1000000
    return total, round(elapsed)

def searchAll(jumpSet, current, found, visited, count):
    
    visited[current] = 1 
    
    if current == found:
        count += 1
    else:
        for j in jumpSet[current]:
            if visited[j] == 0:
                count = searchAll(jumpSet, j, found, visited, count)
                
    visited[current] = 0
    
    return count

# Q2 : 
def q2():

    grid = parseInput()
    start = time.perf_counter()
    
    jumps = defaultdict(list)
    maxRow = len(grid)
    maxCol = len(grid[0])
    
    # Create hash of possible movements
    for rowIndex in range(maxRow):
        for colIndex in range(maxCol):
            for dx, dy in DIRECTIONS:
                nx = rowIndex + dx
                ny = colIndex + dy
                if (0 <= nx < maxRow and 0 <= ny < maxCol and grid[nx][ny] == grid[rowIndex][colIndex] + 1):
                    jumps[(grid[rowIndex][colIndex], rowIndex, colIndex)].append((grid[nx][ny], rowIndex + dx, colIndex + dy))
                else:
                    jumps[(grid[rowIndex][colIndex], rowIndex, colIndex)]
    
    total = 0  
    for j in jumps.keys():
        if j[0] == 0:
            found = search(jumps, j) 
            for trail in found:
                score = 0                    
                visited = {}
                for x in jumps.keys():
                    visited[x] = 0

                total += searchAll(jumps, j, trail, visited, score)

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
