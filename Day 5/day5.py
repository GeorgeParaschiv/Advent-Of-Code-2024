# Day 5 Advent of Code
# Author: George Paraschiv
# Date: 2024-12-05

import time, functools

# Parse Input
def parseInput():
    with open("input.txt", "r") as input:
        sections = input.read().strip().split("\n\n")
        
    rules = [tuple(int(x) for x in line.split("|")) for line in sections[0].splitlines()]
    updates = [[int(x) for x in line.split(",")] for line in sections[1].splitlines()]
    
    return rules, updates

# Function to create set of rules from input
def createRuleSet(rules):
    
    # ruleSet = {page : {set of pages that page must come before}}
    ruleSet = {}
    for rule in rules:
        ruleSet.setdefault(rule[0], set()).add(rule[1])
        
    return ruleSet

# Function to check if update is valid based on rules
def checkUpdate(ruleSet, update):
    
    for pageIndex, page in enumerate(update[:-1]):
        if (page in ruleSet[update[pageIndex+1]]):
            return False
        
    return True

# Q1 : O(u + r)
def q1():
    
    rules, updates = parseInput()
    start = time.perf_counter()
    
    ruleSet = createRuleSet(rules) 
    
    total = sum(update[len(update)//2] for update in updates if checkUpdate(ruleSet, update))
    
    elapsed = (time.perf_counter() - start) * 1000000
    return total, round(elapsed)

# Q2 : O(u*log u + r)
def q2():
    
    rules, updates = parseInput()
    start = time.perf_counter()
     
    ruleSet = createRuleSet(rules)
        
    total = 0
    for update in updates:
        
        if checkUpdate(ruleSet, update):
            continue
    
        update.sort(key=functools.cmp_to_key(lambda x, y: 1 if y in ruleSet[x] else -1))
   
        total += update[len(update)//2]
        
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
