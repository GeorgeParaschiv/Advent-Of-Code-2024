# Day 6 Advent of Code
# Author: George Paraschiv
# Date: 2024-12-06

import cProfile

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# Parse Input
def parseInput():
    with open("input.txt", "r") as input:
        lines = tuple(list(line.rstrip()) for line in input.readlines())
    
    return lines

# Function to find the starting location of the guard
def findStart(grid): 
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "^":
                return row, col

# Function to try a new position on the grid
def tryNewPosition(grid, x, y, direction, visited):
    
    newX, newY = x + direction[0], y + direction[1]
    
    if ((0 <= newX < len(grid)) and (0 <= newY < len(grid[0]))):
        if (grid[newX][newY] == "#"):
            return 1
        else:
            if (grid[newX][newY] not in visited):
                visited.add((newX, newY))
            return 0
    else:
        return -1

# Function to Simulate the Guards Path
def simulate(grid, xPos, yPos, visited=set()):
    
    current = 0
    orientations = [[set() for _ in row] for row in grid]
    
    while (current not in orientations[xPos][yPos]):
    
        orientations[xPos][yPos].add(current) 
        result = tryNewPosition(grid, xPos, yPos, DIRECTIONS[current], visited)
        
        if (result == -1):           
            return True
        elif (result == 0):
            xPos += DIRECTIONS[current][0]
            yPos += DIRECTIONS[current][1]
        else:
            current = (current + 1) % 4
            
    return False   

# Q1 : O(n)
def q1():
    
    lines = parseInput()
    visited = set()
    
    xPos, yPos = findStart(lines)
    
    simulate(lines, xPos, yPos, visited)
                       
    return len(visited) + 1

# Q2 : O(n^2)
def q2():
    
    lines = parseInput()
    visited = set()
    
    xPos, yPos = findStart(lines)

    simulate(lines, xPos, yPos, visited)
    
    sum = 0
    for location in visited:
        lines[location[0]][location[1]] = "#"  
            
        if (not simulate(lines, xPos, yPos)):
            sum += 1 
                    
        lines[location[0]][location[1]] = "."
   
    return sum

# ---------- Main ----------
if __name__ == "__main__":

    print(f"Distinct Positions Visited: {q1()}")   
    print(f"Distinct Obstacle Positions: {q2()}")
