# Day 1 Advent of Code
# Author: George Paraschiv
# Date: 2024-12-01

# Parse Input
def parseInput():
    
    with open("input.txt", "r") as input:
        lines = [line.rstrip().split() for line in input.readlines()]
        
    list1 = [int(line[0]) for line in lines]
    list2 = [int(line[1]) for line in lines]
    
    return list1, list2

# Q1 : O(nlogn)
def q1():
    
    list1, list2 = parseInput()
    
    list1.sort()
    list2.sort()

    diff = 0
    for index, line in enumerate(list1):
        diff += abs(list1[index]-list2[index])

    return diff

# Q2 : O(n)
def q2():
    
    list1, list2 = parseInput()

    # Create hashmap of list2: key = id, value = # of times id appears in list2
    dict2 = {}
    for id in list2:
        if id in dict2:
            dict2[id] += 1
        else:
            dict2[id] = 1

    # Check if item in list 1 is in hashmap and update similarity score
    score = 0
    for id in list1:
        if id in dict2:
            score += id * dict2[id]

    return score

# ---------- Main ----------
if __name__ == "__main__":

    print(f"Total Difference: {q1()}")  
    print(f"Similarity Score: {q2()}")