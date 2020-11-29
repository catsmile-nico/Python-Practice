# https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true

# Task
# The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].
    # If a[i] > b[i], then Alice is awarded 1 point.
    # If a[i] < b[i], then Bob is awarded 1 point.
    # If a[i] = b[i], then neither person receives a point.
# Comparison points is the total points a person earned.
# Given a and b, determine their respective comparison points.

# Example
# a = [1, 2, 3]
# b = [3, 2, 1]

    # For elements *0*, Bob is awarded a point because a[0] .
    # For the equal elements a[1] and b[1], no points are earned.
    # Finally, for elements 2, a[2] > b[2] so Alice receives a point.

# The return array is [1, 1] with Alice's score first and Bob's second. 

# Input Format
# The first line contains 3 space-separated integers, a[0], a[1], and a[2], the respective values in triplet a.
# The second line contains 3 space-separated integers, b[0], b[1], and b[2], the respective values in triplet b.

# Constraints
# 1 ≤ a[i] ≤ 100
# 1 ≤ b[i] ≤ 100

# Sample Input 0
# 5 6 7
# 3 6 10

# Sample Output 0
# 1 1


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    a_score = 0
    b_score = 0

    for _ in range(len(a)):
        if a[_] > b[_]:
            a_score += 1
        elif b[_] > a[_]:
            b_score += 1
    
    return (a_score, b_score)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
