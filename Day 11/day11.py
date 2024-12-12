# Day 11 Advent of Code
# Author: George Paraschiv
# Date: 2024-12-11

import time, math

# Parse Input
def parseInput():
    with open("input.txt", "r") as input:
        line = [int(x) for x in list(input.readline().rstrip().split())]
    
    return line

def transform(stone, cache):
    
    if stone in cache:
        return cache[stone]
    
    if stone == 0:
        result = [1]  
    elif len(str(stone)) % 2 == 0:
        mid = len(str(stone)) // 2
        result = [int(str(stone)[:mid]), int(str(stone)[mid:])]
    else:
        result = [stone * 2024]  
        
    cache[stone] = result
    return result

def performBlinks(blinks, stones, cache={}):
    
    for _ in range(blinks):
        new = {}
        for stone, count in stones.items():               
            for stone in transform(stone, cache):
                if stone in new:
                    new[stone] += count
                else:
                    new[stone] = count
                
        stones = new

    return sum(stones.values())

# Q1 : 
def q1():

    input = parseInput()
    start = time.perf_counter()
    
    stones = {key : 1 for key in input}
    
    total = performBlinks(25, stones)        

    elapsed = (time.perf_counter() - start) * 1000000
    return total, round(elapsed)

# Q2 : 
def q2():

    input = parseInput()
    start = time.perf_counter()
        
    stones = {key : 1 for key in input}
    
    total = performBlinks(75, stones)     

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
