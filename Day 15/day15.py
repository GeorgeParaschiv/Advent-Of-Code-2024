# Day 15 Advent of Code
# Author: George Paraschiv
# Date: 2024-12-15

import time

DIRECTIONS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

# Parse Input
def parseInput():
    with open("input.txt", "r") as input:
        lines = input.read().split("\n\n")

        #print(lines)
        
        grid = [list(row) for row in lines[0].split("\n")]
        movements = [col for row in lines[1].split("\n") for col in row]
        
    return grid, movements

def printGrid(grid, MAXCOL):
    for row, col in grid.keys():
        
        if (col < MAXCOL-1):
            print(grid[(row, col)], end="")
        else:
            print(grid[(row, col)])        

# Q1 : 
def q1():

    input = parseInput()
    start = time.perf_counter()
    
    
    grid = {}
    movements = input[1]
    MAXCOL = len(input[0][0])
    
    for rowIndex in range(len(input[0])):
        for colIndex in range(len(input[0][0])):
            grid[(rowIndex, colIndex)] = input[0][rowIndex][colIndex]
            
            if input[0][rowIndex][colIndex] == '@':
                x, y = rowIndex, colIndex                  
    
    for movement in movements:
        
        dx, dy = DIRECTIONS[movement]
        
        if (grid[(x+dx, y+dy)] == "#"):
                    
            # print("Move " + movement)     
            # printGrid(grid, MAXCOL)
            # print()
            
            continue
        elif (grid[(x+dx, y+dy)] == "."):
            grid[(x,y)] = "."
            grid[(x+dx, y+dy)] = "@"            
        else:
            nx, ny = x + 2*dx, y + 2*dy
            
            while(grid[(nx, ny)] == "O"):
                nx, ny = nx + dx, ny + dy
                             
            if (grid[(nx, ny)] == "#"):
                continue
            else:
                grid[(nx, ny)] = "O"
                grid[(x+dx, y+dy)] = "@"
                grid[(x,y)] = "."
        
        x,y = x+dx, y+dy
         
        # print("Move " + movement)     
        # printGrid(grid, MAXCOL)
        # print()
    
    total = 0 
    for x,y in grid.keys():
        if (grid[(x, y)] == "O"):
            total += (x * 100 + y)           

    

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
