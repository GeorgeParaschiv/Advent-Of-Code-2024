# Day 14 Advent of Code
# Author: George Paraschiv
# Date: 2024-12-14

import time, re
from collections import defaultdict

MAXCOL = 101
MAXROW = 103

# Parse Input
def parseInput():
    with open("input.txt", "r") as input:
        lines = input.read()
        pattern = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"      
        
    return [list(int(x) for x in match) for match in re.findall(pattern, lines)]

def simulate(positions, velocities):
    
    for index, p in enumerate(positions):
        positions[index] = ((p[0] + velocities[index][0] + MAXROW) % MAXROW, (p[1] + velocities[index][1] + MAXCOL) % MAXCOL)

def printGrid(positions):
    
    pos = defaultdict(lambda:0)
    for p in positions:
        pos[p] += 1
            
    for x in range(MAXROW):
        for y in range(MAXCOL):
            if (x, y) in pos:
                print(pos[(x,y)], end="")
            else:
                print(".", end="")
        print()

# Q1 : 
def q1():

    input = parseInput()
    start = time.perf_counter()

    velocities = []
    positions = []
    
    for robot in input:
        positions.append((robot[1], robot[0]))
        velocities.append((robot[3], robot[2]))
       
    for _ in range(100):
        simulate(positions, velocities)
    
    q1, q2, q3, q4 = 0, 0, 0, 0
    
    for p in positions:
        if (p[0] < MAXROW//2):
            if (p[1] < MAXCOL//2):
                q1 += 1
            elif (p[1] > MAXCOL//2):
                q2 += 1
        elif (p[0] > MAXROW//2):
            if (p[1] < MAXCOL//2):
                q3 += 1
            elif (p[1] > MAXCOL//2):
                q4 += 1
    
    total = q1 * q2 * q3 * q4    

    elapsed = (time.perf_counter() - start) * 1000000
    return total, round(elapsed)

def adjacency(positions):
    
    pos = set(positions)
    
    score = 0
    for p in pos:
        if (p[0] - 1, p[1]) in pos:
            score += 1
            
    return score        

# Q2 : 
def q2():

    input = parseInput()
    start = time.perf_counter()
    
    velocities = []
    positions = []
    
    for robot in input:
        positions.append((robot[1], robot[0]))
        velocities.append((robot[3], robot[2]))
       
    score = 0
    total = 0
    while (score < 80):
        simulate(positions, velocities)
        score = adjacency(positions)
        total += 1
        
    #printGrid(positions)

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
