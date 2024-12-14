# Day 13 Advent of Code
# Author: George Paraschiv
# Date: 2024-12-13

import time, re, cProfile

# Parse Input
def parseInput():
    with open("input.txt", "r") as input:
        lines = input.read()
        
        pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"      
        
        return [tuple(int(x) for x in match)for match in re.findall(pattern, lines)]

# Q1 : O(n)
def q1():

    input = parseInput()
    start = time.perf_counter()

    total = 0
    
    for game in input:
        xnum = (game[2]*game[5] - game[3]*game[4]) 
        xdiv = (game[1]*game[2] - game[0]*game[3])
        
        if (xnum % xdiv != 0):
            continue
        
        ynum = game[4] - game[0]*(xnum//xdiv)
        
        if (ynum % game[2] != 0):
            continue
        
        total += (xnum//xdiv) * 3 + (ynum//game[2])

    elapsed = (time.perf_counter() - start) * 1000000
    return total, round(elapsed)

# Q2 : O(n)
def q2():

    input = parseInput()
    start = time.perf_counter()
    
    total = 0
    for game in input:
        
        new4 = game[4] + 10000000000000
        new5 = game[5] + 10000000000000
        
        xnum = (game[2]*new5 - game[3]*new4) 
        xdiv = (game[1]*game[2] - game[0]*game[3])
        
        if (xnum % xdiv != 0):
            continue
        
        ynum = new4 - game[0]*(xnum//xdiv)
        
        if (ynum % game[2] != 0):
            continue
        
        total += (xnum//xdiv) * 3 + (ynum//game[2])

    elapsed = (time.perf_counter() - start) * 1000000
    return total, round(elapsed)

# ---------- Main ----------
if __name__ == "__main__":

    #cProfile.run("q1()")
    
    sol1, time1 = q1()
    print(f"Part 1 Solution: {sol1}")
    print(f"Part 1 Time: {time1} us") 
    
    sol2, time2 = q2()
    print(f"Part 2 Solution: {sol2}")
    print(f"Part 2 Time: {time2} us")
