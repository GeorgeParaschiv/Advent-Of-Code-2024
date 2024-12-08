# Day 7 Advent of Code
# Author: George Paraschiv
# Date: 2024-12-07

from itertools import product

operators = ["+", "*"]

# Q1 : 
def q1(input):

    total = 0
    for line in input:  
        comboList = product(operators, repeat=len(line)-2)
        
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
                    sum = sum * (10**len(line[index+2])) + int(line[index+2])
          
            
            if (sum == int(line[0])):
                total += int(line[0])
                break  
        
    return total

# Q2 : 
def q2(input):
    
    operators.append("||")
    return q1(lines)

# ---------- Main ----------
if __name__ == "__main__":

    # Parse Input
    with open("input.txt", "r") as input:
        lines = [line.rstrip().replace(":", "").split() for line in input.readlines()]

    print(f"Total calibration result is: {q1(lines)}")
    print(f"Second calibration result is: {q2(lines)}")
