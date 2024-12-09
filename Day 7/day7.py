# Day 7 Advent of Code
# Author: George Paraschiv
# Date: 2024-12-07

from itertools import product

OPERATORS = {"+", "*"}

POWERS = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000,
          1000000000, 10000000000, 100000000000, 1000000000000, 10000000000000, 
          100000000000000, 1000000000000000, 10000000000000000]

# Parse Input
def parseInput():
    with open("input.txt", "r") as input:
        lines = [line.rstrip().replace(":", "").split() for line in input.readlines()]
    
    return lines

# Q1 : O(2^n)
def q1():

    input = parseInput()
    
    total = 0
    for line in input:  
        comboList = product(OPERATORS, repeat=len(line)-2)
        
        for opList in comboList:
            sum = int(line[1])
            for index in range(len(opList)):
                
                if (sum > int(line[0])):
                    break
                
                if (opList[index] == "+"):
                    sum += int(line[index+2])
                elif (opList[index] == "*"):
                    sum *= int(line[index+2])
                else:
                    sum = (sum * POWERS[len(line[index+2])]) + int(line[index+2])
          
            
            if (sum == int(line[0])):
                total += int(line[0])
                break  
        
    return total

# Q2 : O(3^n)
def q2():
    
    OPERATORS.add("||")
    return q1()

# ---------- Main ----------
if __name__ == "__main__":

    print(f"First Calibration Result: {q1()}")
    print(f"Second Calibration Result: {q2()}")
