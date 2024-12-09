# Day 8 Advent of Code
# Author: George Paraschiv
# Date: 2024-12-08

import time

# Parse Input
def parseInput():
    with open("input.txt", "r") as input:
        lines = [list(line.rstrip()) for line in input.readlines()]
    
    return lines

# Function to try a new grid position
def tryPosition(grid, nodes, x, y):
    
    if (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            nodes.add((x, y))
            return True
    else:
        False

# Q1 : O(n^2)
def q1():

    grid = parseInput()
    start = time.perf_counter()
    
    antennaDict = dict()

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (grid[row][col] != "."):
                antennaDict.setdefault(grid[row][col], []).append((row, col))
    
    antinodes = set()
    for antennaKey in antennaDict.keys():
        for antenna1 in range(len(antennaDict[antennaKey]) - 1):
            for antenna2 in range(antenna1+1, len(antennaDict[antennaKey])):
                x1, y1 = antennaDict[antennaKey][antenna1]
                x2, y2 = antennaDict[antennaKey][antenna2]
                diffx = abs(x2 - x1)
                diffy = abs(y2 - y1)
                
                # North East and South West
                if (y1 >= y2):
                    tryPosition(grid, antinodes, x1 - diffx, y1 + diffy)
                    tryPosition(grid, antinodes, x2 + diffx, y2 - diffy)
                elif (y1 < y2): # North West and South East
                    tryPosition(grid, antinodes, x1 - diffx, y1 - diffy)
                    tryPosition(grid, antinodes, x2 + diffx, y2 + diffy)
    
    total = len(antinodes)
      
    elapsed = (time.perf_counter() - start) * 1000000
    return len(antinodes), round(elapsed)

def tryAllPositions(grid, nodes, x1, x2, y1, y2, diffx, diffy):
    
    if (y1 >= y2):
        
        i = 1
        while(tryPosition(grid, nodes, x1 - i *diffx, y1 + i * diffy)):
            i += 1
            
        i = 1
        while(tryPosition(grid, nodes, x2 + i *diffx, y2 - i * diffy)):
            i += 1
            
    elif (y1 < y2):
        
        i = 1
        while(tryPosition(grid, nodes, x1 - i *diffx, y1 - i * diffy)):
            i += 1
            
        i = 1
        while(tryPosition(grid, nodes, x2 + i *diffx, y2 + i * diffy)):
            i += 1 
    
    return

# Q2 : O(n^2)
def q2():

    grid = parseInput()
    start = time.perf_counter()
    
    antennaDict = dict()

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (grid[row][col] != "."):
                antennaDict.setdefault(grid[row][col], []).append((row, col))
    
    antinodes = set()
    for antennaKey in antennaDict.keys():
        for antenna1 in range(len(antennaDict[antennaKey]) - 1):
            for antenna2 in range(antenna1+1, len(antennaDict[antennaKey])):
                x1, y1 = antennaDict[antennaKey][antenna1]
                x2, y2 = antennaDict[antennaKey][antenna2]
                diffx = abs(x2 - x1)
                diffy = abs(y2 - y1)
                
                antinodes.add((x1, y1))
                antinodes.add((x2, y2))
                
                tryAllPositions(grid, antinodes, x1, x2, y1, y2, diffx, diffy)
    
    total = len(antinodes)
    
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
