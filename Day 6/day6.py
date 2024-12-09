# Day 6 Advent of Code
# Author: George Paraschiv
# Date: 2024-12-06

import time

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# Parse Input
def parseInput():
    with open("input.txt", "r") as input:
        lines = tuple(list(line.rstrip()) for line in input.readlines())
    
    return lines

# Function to find the starting location of the guard
def findStart(grid): 
    for row in grid:
        for col in row:
            if col == "^":
                return grid.index(row), row.index(col)    

# Function to Simulate the Guards Path
def simulate(grid, xPos, yPos):
    
    current = 0
    visited = set()
    orientations = [[[] for _ in row] for row in grid]
    
    while (current not in orientations[xPos][yPos]):
    
        orientations[xPos][yPos].append(current) 
        
        newX, newY = xPos + DIRECTIONS[current][0], yPos + DIRECTIONS[current][1]
    
        if ((0 <= newX < len(grid)) and (0 <= newY < len(grid[0]))):
            if (grid[newX][newY] == "#"):
                current = (current + 1) % 4
            else:
                visited.add((newX, newY))
                xPos, yPos = newX, newY
        else:
            return visited
            
    return False   

# Q1 : O(n)
def q1():
    
    lines = parseInput()
    start = time.perf_counter()
    
    xPos, yPos = findStart(lines)
    visited = simulate(lines, xPos, yPos)
    
    total = len(visited) + 1
                       
    elapsed = (time.perf_counter() - start) * 1000000
    return total, round(elapsed)

# Q2 : O(n^2)
def q2():
    
    lines = parseInput()
    start = time.perf_counter()
    
    xPos, yPos = findStart(lines)
    visited = simulate(lines, xPos, yPos)
    
    total = 0
    for location in visited:
        lines[location[0]][location[1]] = "#"  
            
        if (not simulate(lines, xPos, yPos)):
            total += 1 
                    
        lines[location[0]][location[1]] = "."
   
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
