# Day 5 Advent of Code
# Author: George Paraschiv
# Date: 2024-12-05

# Check if update is valid based on rules : O(u + r)
def checkUpdate(ruleSet, update):
    
    # Create a dict for every page in the updates with value being the index in 
    indexDict = {page : index for index, page in enumerate(update)}
    
    # For every rule check that x does not come before y in the update
    for x,y in rules:
        if x in indexDict and y in indexDict and indexDict[x] > indexDict[y]:
            return False
        
    return True

# Q1 : O(u * r)
def q1(rules, updates):
    
    # Create dict where a keys values are a set of pages that must come before the key page   
    ruleSet = {}
    for rule in rules:
        ruleSet.setdefault(rule[0], set()).add(rule[1])
    
    correctUpdates = [update for update in updates if checkUpdate(ruleSet, update)]
    
    return sum(int(update[len(update)//2]) for update in correctUpdates)


# Q2 : O(u * log u + r)
def q2(rules, updates):
    
    # Create dict where a keys values are a set of pages that must come before the key page   
    ruleSet = {}
    for rule in rules:
        ruleSet.setdefault(rule[0], set()).add(rule[1])
    
    sum = 0
    for update in updates:
        
        if checkUpdate(rules, update):
            continue
        
        for page in range(len(update) - 1):
            for other in range(page+1, len(update)):
                if (update[page] in ruleSet.get(update[other], "")):
                    update[page], update[other] = update[other], update[page] 
   
        sum += int(update[len(update)//2])
    
    return sum

# ---------- Main ----------
if __name__ == "__main__":

    # Parse Input
    with open("input.txt", "r") as input:
        sections = input.read().strip().split("\n\n")
        
    rules = [tuple(int(x) for x in line.split("|")) for line in sections[0].splitlines()]
    updates = [[int(x) for x in line.split(",")] for line in sections[1].splitlines()]

    print(f"Sum of correct update middle values is {q1(rules, updates)}")
    print(f"Sum of corrected update middle values is {q2(rules, updates)}")
