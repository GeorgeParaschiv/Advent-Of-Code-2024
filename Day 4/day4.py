# Day 4 Advent of Code
# Author: George Paraschiv
# Date: 2024-12-04   

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
def search(grid, x, y):
    
    def validString(dx, dy):

        check = ""

        for i in range(4):
            nx = x + dx * i
            ny = y + dy * i

            if (0 <= nx < len(grid) and 0 <= ny < len(grid[nx])):
                check += grid[nx][ny]
            else:
                return ""
            
        return check
    
    return sum(1 for dx, dy in DIRECTIONS if validString(dx, dy) == "XMAS")

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
    
    xmasCount = 0

    # Search for first letter than call search algorithm at that index
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (grid[row][col] == "X"):

                xmasCount += search(grid, row, col)

    return xmasCount

# Q2 : O(n)
def q2():

    grid = parseInput()
    
    masxCount = 0

    for row in range(1, len(grid)-1):
        for col in range(1, len(grid[row])-1):
            if (grid[row][col] == "A"):

                masxCount += xSearch(grid, row, col)

    return masxCount

# ---------- Main ----------
if __name__ == "__main__":

    print(f"XMAS Count: {q1()}")
    print(f"MAS-X Count: {q2()}")
