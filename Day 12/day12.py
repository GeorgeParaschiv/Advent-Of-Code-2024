# Day 12 Advent of Code
# Author: George Paraschiv
# Date: 2024-12-12

import time
from collections import defaultdict, deque

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# Parse Input
def parseInput():
    with open("input.txt", "r") as input:
        lines = [list(line.rstrip()) for line in input.readlines()]
    
    return lines

def findRegions(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    regions = defaultdict(list)

    def bfs(start):
        queue = deque([start])
        region = []
        plant = grid[start[0]][start[1]]
        
        while queue:       
            x, y = queue.popleft()
            
            if visited[x][y]:
                continue
            
            visited[x][y] = True
            region.append((x, y))
            
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] == plant:
                    queue.append((nx, ny))
                    
        return region

    for rowIndex in range(rows):
        for colIndex in range(cols):
            if not visited[rowIndex][colIndex]:
                region = bfs((rowIndex, colIndex))
                regions[grid[rowIndex][colIndex]].append(region)

    return regions

def calcPerimeter(region, grid):
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for x, y in region:
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < rows and 0 <= ny < cols) or grid[nx][ny] != grid[x][y]:
                perimeter += 1

    return perimeter

# Q1 : 
def q1():

    grid = parseInput()
    start = time.perf_counter()
    
    regions = findRegions(grid)
    total = 0 

    for _, regionList in regions.items():
        for region in regionList:
            perimeter = calcPerimeter(region, grid)
            total += len(region) * perimeter         

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
