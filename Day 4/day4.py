# Day 4 Advent of Code
# Author: George Paraschiv
# Date: 2024-12-04   

import time, cProfile

DIRECTIONS = [
        (-1,  0),  # North
        (-1,  1),  # North East
        ( 0,  1),  # East
        ( 1,  1),  # South East
        ( 1,  0),  # South
        ( 1, -1),  # South West
        ( 0, -1),  # West
        (-1, -1)   # North West
]

# Parse Input
def parseInput():
    with open("input.txt", "r") as input:
        grid = [line.rstrip() for line in input.readlines()]
    
    return grid

# Function to check all options of the word search 
def search(grid, rows, cols, x, y):
    
    target = "XMAS"
    total = 0
    
    for dx, dy in DIRECTIONS:
        valid = True
        for i in range(4):
            nx = x + dx * i
            ny = y + dy * i

            if (not (0 <= nx < rows and 0 <= ny < cols) or grid[nx][ny] != target[i]):
                valid = False
                break
        
        if valid:  
            total += 1
    
    return total

# Function to check if MAS X exists
def xSearch(grid, x, y):

    cross = {"S", "M"}

    if ({grid[x-1][y-1], grid[x+1][y+1]} == cross) and ({grid[x-1][y+1], grid[x+1][y-1]} == cross):
        return 1
    else:
        return 0

# Q1 : O(n)
def q1():

    grid = parseInput()
    start = time.perf_counter()
    
    total = 0

    # Search for first letter than call search algorithm at that index
    maxRows = len(grid)
    maxCols = len(grid[0])
    for row in range(maxRows):
        for col in range(maxCols):
            if (grid[row][col] == "X"):               
                total += search(grid, maxRows, maxCols, row, col)

    elapsed = (time.perf_counter() - start) * 1000000
    return total, round(elapsed)

# Q2 : O(n)
def q2():

    grid = parseInput()
    start = time.perf_counter()
    
    total = 0

    maxRows = len(grid) - 1
    maxCols = len(grid[0]) - 1
    for row in range(1, maxRows):
        for col in range(1, maxCols):
            if (grid[row][col] == "A"):
                total += xSearch(grid, row, col)

    elapsed = (time.perf_counter() - start) * 1000000
    return total, round(elapsed)

# ---------- Main ----------
if __name__ == "__main__":

    cProfile.run("q2()")

    sol1, time1 = q1()
    print(f"Part 1 Solution: {sol1}")
    print(f"Part 1 Time: {time1} us") 
    
    sol2, time2 = q2()
    print(f"Part 2 Solution: {sol2}")
    print(f"Part 2 Time: {time2} us")
