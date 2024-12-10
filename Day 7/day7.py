# Day 7 Advent of Code
# Author: George Paraschiv
# Date: 2024-12-07

import time
from itertools import product

POWERS = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000,
          1000000000, 10000000000, 100000000000, 1000000000000, 10000000000000, 
          100000000000000, 1000000000000000, 10000000000000000]

# Parse Input
def parseInput():
    with open("input.txt", "r") as input:
        lines = [[int(x) for x in line.rstrip().replace(":", "").split()] for line in input.readlines()]
    
    return lines

# Function to precompute the permutations
def computeCombos(operators):
    
    combos = []
    for i in range(1, 12):
        combos.append(list(product(operators, repeat=i)))
        
    return combos

# Function to check each combination starting from the end
def checkCombinations(line, comboList):
    
    target = line[1]
    
    for opList in comboList:
        total = line[0]
        for index in range(len(opList)-1, -1, -1):
            
            num = line[index+2]
            
            if (opList[index] == 0):
                total -= num
            elif (opList[index] == 1):
                if total % num == 0:
                    total //= num
                else:
                    break        
            else:
                divisor = POWERS[len(str(num))]
                
                if total % divisor != num:
                    break
                else:
                    total //= divisor 
        
        if (total == target):
            return line[0]
        
    return 0

# Q1 : O(2^n)
def q1():

    input = parseInput()
    start = time.perf_counter()
    
    # 0 = "+", 1 = "*"
    operators = [0, 1]
    comboLists = computeCombos(operators)
    
    total = 0
    for line in input:          
        total += checkCombinations(line, comboLists[len(line) - 3]) 
        
    elapsed = (time.perf_counter() - start) * 1000000
    return total, round(elapsed)

# Q2 : O(3^n)
def q2():
    
    input = parseInput()
    start = time.perf_counter()
    
    # 0 = "+", 1 = "*", 2 = "||"
    operators = [0, 1, 2]
    comboLists = computeCombos(operators)
    
    total = 0
    for line in input:          
        total += checkCombinations(line, comboLists[len(line) - 3]) 
    
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
