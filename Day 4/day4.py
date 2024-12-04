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

# Function to check all options of the word earch 
def search(x, y, word):
    
    def validString(dx, dy):

        check = ""

        for i in range(len(word)):
            nx = x + dx * i
            ny = y + dy * i

            if (0 <= nx < len(grid) and 0 <= ny < len(grid[nx])):
                check += grid[nx][ny]
            else:
                return ""
            
        return check
    
    return sum(1 for dx, dy in DIRECTIONS if validString(dx, dy) == word)

# Function to check if MAS X exists
def xSearch(x, y):

    cross = {"S", "M"}

    if ({grid[x-1][y-1], grid[x+1][y+1]} == cross) and ({grid[x-1][y+1], grid[x+1][y-1]} == cross):
        return 1
    else:
        return 0

# Q1 : O(n)
def q1(word):

    xmasCount = 0

    # Search for first letter than call search algorithm at that index
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (grid[row][col] == word[0]):

                xmasCount += search(row, col, word)

    return xmasCount

# Q2 : O(n)
def q2():

    masxCount = 0

    for row in range(1, len(grid)-1):
        for col in range(1, len(grid[row])-1):
            if (grid[row][col] == "A"):

                masxCount += xSearch(row, col)

    return masxCount

# ---------- Main ----------
if __name__ == "__main__":

    # Parse Input
    with open("input.txt", "r") as input:
        grid = [line.rstrip() for line in input.readlines()]

    print(f"XMAS count: {q1("XMAS")}")
    print(f"MAS X count: {q2()}")
