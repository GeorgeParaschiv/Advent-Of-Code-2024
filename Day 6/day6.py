# Day 6 Advent of Code
# Author: George Paraschiv
# Date: 2024-12-06

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def tryNewPosition(grid, x, y, direction):
    
    newX, newY = x + direction[0], y + direction[1]
    
    if ((0 <= newX < len(grid)) and (0 <= newY < len(grid[0]))):
        if (grid[newX][newY] == "."):
            grid[newX][newY] = "X"
            return 1
        elif (grid[newX][newY] == "X" or grid[newX][newY] == "^"):
            return 0
        else:
            return 2
    else:
        return -1

# Q1 : O(n)
def q1(lines):

    grid = [[col for col in row] for row in lines]
    orientations = [[[] for col in row] for row in grid]
    xPos = 0 
    yPos = 0
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "^":
                xPos = row
                yPos = col
    
    count = 1   
    current = 0 
    while (current not in orientations[xPos][yPos]):
    
        orientations[xPos][yPos].append(current) 
        result = tryNewPosition(grid, xPos, yPos, DIRECTIONS[current])
        
        if (result == -1):           
            return count, grid
        elif (result == 0 or result == 1):
            count += result
            xPos += DIRECTIONS[current][0]
            yPos += DIRECTIONS[current][1]
        else:
            current = (current + 1) % 4      

    return 0, grid

# Q2 : O(n^2)
def q2(lines):
    
    grid = q1(lines)[1]
    
    sum = 0
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if (grid[row][col] == "X"): 
                lines[row][col] = "#"  
                     
                if (q1(lines)[0] == 0):
                    sum += 1 
                          
                lines[row][col] = "."
   
    return sum

# ---------- Main ----------
if __name__ == "__main__":

    # Parse Input
    with open("input.txt", "r") as input:
        lines = tuple(list(line.rstrip()) for line in input.readlines())
    
    print(f"Distinct positions visited: {q1(lines)[0]}")
    
    print(f"Distinct obstacle positions: {q2(lines)}")
