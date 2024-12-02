import os
import math

# Q1 : O(nlogn)
def q1(list1, list2):
    
    list1.sort()
    list2.sort()

    diff = 0
    for index, line in enumerate(list1):
        diff += abs(list1[index]-list2[index])

    print(f"Total Difference is: {diff}")

# Q2 : O(n)
def q2(list1, list2):

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

    print(f"Similarity Score is: {score}")

# Main
if __name__ == "__main__":

    l1 = []
    l2 = []

    # Parse input into two lists
    with open("input.txt", "r") as input:
        lines = input.readlines()

        for line in lines:
            line = line.split()
            l1.append(int(line[0]))
            l2.append(int(line[1]))

    q1(l1, l2)
    q2(l1, l2)