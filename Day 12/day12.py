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
        perimeter = 0
        
        while queue:       
            x, y = queue.popleft()
            
            if visited[x][y]:
                continue
            
            visited[x][y] = True
            region.append((x, y))
            
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                
                if not (0 <= nx < rows and 0 <= ny < cols) or grid[nx][ny] != grid[x][y]:
                    perimeter += 1
                
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] == plant:
                    queue.append((nx, ny))
                    
        return region, perimeter

    for rowIndex in range(rows):
        for colIndex in range(cols):
            if not visited[rowIndex][colIndex]:
                region, perimeter = bfs((rowIndex, colIndex))
                regions[grid[rowIndex][colIndex]].append((region, perimeter))

    return regions

# Q1 : O(n)
def q1():

    grid = parseInput()
    start = time.perf_counter()
    
    regions = findRegions(grid)
    total = 0 

    for regionList in regions.values():
        for region in regionList:
            total += len(region[0]) *  region[1]        

    elapsed = (time.perf_counter() - start) * 1000000
    return total, round(elapsed)

def calculateEdges(region):
    
    vertices = defaultdict(lambda:0)

    for x,y in region:
        vertices[(x,y)] += 1
        vertices[(x+1,y)] += 1
        vertices[(x,y+1)] += 1
        vertices[(x+1,y+1)] += 1
     
    edges = 0   
    for pos, vertex in vertices.items():
        if vertex % 2 == 1:
            edges += 1
        elif vertex == 2 and (((pos[0],pos[1]) in region and (pos[0]-1,pos[1]-1) in region) or ((pos[0],pos[1]-1) in region and (pos[0]-1, pos[1]) in region)):
            edges += 2
    
    return edges

# Q2 : 
def q2():

    grid = parseInput()
    start = time.perf_counter()
    
    regions = findRegions(grid)
    total = 0 

    for regionList in regions.values():
        for region in regionList:
            total += len(region[0]) * calculateEdges(region[0])

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
