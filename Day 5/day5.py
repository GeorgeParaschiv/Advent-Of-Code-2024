# Day 5 Advent of Code
# Author: George Paraschiv
# Date: 2024-12-05

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
    ruleSet = createRuleSet(rules) 
    
    correctUpdates = [update for update in updates if checkUpdate(ruleSet, update)]
    
    return sum(int(update[len(update)//2]) for update in correctUpdates)

# Q2 : O(u*(u + r))
def q2():
    
    rules, updates = parseInput() 
    ruleSet = createRuleSet(rules)
        
    sum = 0
    for update in updates:
        
        if checkUpdate(ruleSet, update):
            continue
        
        for page in range(len(update) - 1):
            for other in range(page+1, len(update)):
                if (update[page] in ruleSet.get(update[other], "")):
                    update[page], update[other] = update[other], update[page] 
   
        sum += int(update[len(update)//2])
    
    return sum

# ---------- Main ----------
if __name__ == "__main__":

    print(f"Correct Update Middle Value Sum: {q1()}")
    print(f"Corrected Update Middle Value Sum: {q2()}")
