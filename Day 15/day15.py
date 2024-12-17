# Day 15 Advent of Code
# Author: George Paraschiv
# Date: 2024-12-15

import time
from collections import deque, defaultdict

DIRECTIONS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
BOX = {"[", "]"}

# Parse Input
def parseInput():
    with open("input.txt", "r") as input:
        lines = input.read().split("\n\n")

        #print(lines)
        
        grid = [list(row) for row in lines[0].split("\n")]
        movements = [col for row in lines[1].split("\n") for col in row]
        
    return grid, movements

def printGrid(grid):
    
    for row in grid:
        for col in row:
            print(col, end="")
        print() 
    print()      

# Q1 : 
def q1():

    input = parseInput()
    start = time.perf_counter()
    
    
    grid = input[0]
    movements = input[1]
    
    for rowIndex in range(len(grid)):
        for colIndex in range(len(grid[0])):            
            if grid[rowIndex][colIndex] == '@':
                x, y = rowIndex, colIndex 
                break                 
   
    
    for movement in movements:
        
        dx, dy = DIRECTIONS[movement]
        nx, ny = x + dx, y + dy
        
        if (grid[nx][ny] == "#"):            
            continue
        elif (grid[nx][ny] == "."):
            grid[x][y] = "."
            grid[nx][ny] = "@"            
        else:
            nx, ny = nx + dx, ny + dy
            
            while(grid[nx][ny] == "O"):
                nx, ny = nx + dx, ny + dy
                             
            if (grid[nx][ny] == "#"):
                continue
            else:
                grid[nx][ny] = "O"
                grid[x + dx][y + dy] = "@"
                grid[x][y] = "."
        
        x,y = x+dx, y+dy
    
    total = 0 
    for x in range(len(grid)):
        for y in range(len(grid[0])): 
            if (grid[x][y] == "O"):
                total += (x * 100 + y)           

    elapsed = (time.perf_counter() - start) * 1000000
    return total, round(elapsed)

def performMovement(grid, tree, x, y, dx, index):   
    
    for nx, ny in tree[(x, y)]:
        performMovement(grid, tree, nx, ny, dx, index)
    
    if (grid[x][y] == "["):  
        grid[x+dx][y], grid[x+dx][y+1] = grid[x][y], grid[x][y+1]    
        grid[x][y], grid[x][y+1] = ".", "."  

# Q2 : 
def q2():

    input = parseInput()
    start = time.perf_counter()
    
    grid = input[0]
    temp = []
    movements = input[1]
    
    # Remake Grid and find Start
    for rowIndex in range(len(grid)):
        temp.append([])
        for colIndex in range(len(grid[0])):
            if grid[rowIndex][colIndex] == 'O':
                temp[rowIndex].append("[") 
                temp[rowIndex].append("]")
            
            elif grid[rowIndex][colIndex] == '@':
                temp[rowIndex].append("@")
                temp[rowIndex].append(".")
                x, y = rowIndex, colIndex*2   
                
            else:
                temp[rowIndex].append(grid[rowIndex][colIndex])
                temp[rowIndex].append(grid[rowIndex][colIndex])
    grid = temp
     
    # Iterate Through Movements          
    for index, movement in enumerate(movements):
        
        #print("Moving " + movement)        
        dx, dy = DIRECTIONS[movement]
        nx, ny = x + dx, y + dy
        
        if (grid[nx][ny] == "#"):
            continue
        elif (grid[nx][ny] == "."):
            grid[x][y] = "."
            grid[nx][ny] = "@"          
        else:
            
            # If Pushing Right or Left
            if (dx == 0):
                ny += dy
                
                while(grid[nx][ny] in BOX):
                    ny += dy
                                
                if (grid[nx][ny] == "#"):
                    continue
                else:
                    for i in range(ny, y, -dy):
                        grid[nx][i] = grid[nx][i-dy]
                    grid[nx][y + dy] = "@"
                    grid[nx][y] = "."
                    
            # Moving Up or Down
            else:  
                # Create Root of Tree
                if (grid[nx][ny] == "]"):
                    ny -= 1
                      
                tree = defaultdict(list)
                que = deque([(nx, ny)])
                rootx, rooty = nx, ny
                possible = True
                
                while(que):
                
                    nx, ny = que.popleft()
                    
                    # #        #      []    []
                    # []  or  []  or  #  or  #
                    if grid[nx+dx][ny] == "#" or grid[nx+dx][ny+1] == "#":
                        possible = False
                        break
                    
                    # []
                    # []
                    if (grid[nx+dx][ny] == "["): 
                        tree[(nx, ny)].append((nx+dx, ny))
                        que.append((nx+dx, ny))
                    else:
                        
                        # [].       []
                        #  []  or  [].
                        if (grid[nx+dx][ny] == "]"): 
                            if (nx+dx, ny-1) not in tree[(nx, ny-2)]:
                                tree[(nx, ny)].append((nx+dx, ny-1))
                                que.append((nx+dx, ny-1))
                                
                        # .[]      []
                        # []   or  .[]     
                        if (grid[nx+dx][ny+1] == "["): 
                            tree[(nx, ny)].append((nx+dx, ny+1))
                            que.append((nx+dx, ny+1))        
                
                if (possible):
                    performMovement(grid, tree, rootx, rooty, dx, index)
                    grid[x][y] = "."
                    grid[x + dx][y + dy] = "@"
                    x, y = x + dx, y + dy  

                continue
                        
        x, y = x + dx, y + dy 
    
    total = 0 
    for x in range(len(grid)):
        for y in range(len(grid[0])): 
            if (grid[x][y] == "["):
                total += (x * 100 + y)      

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
