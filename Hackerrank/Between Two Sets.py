# https://www.hackerrank.com/challenges/between-two-sets/problem?isFullScreen=true

# Input Format

# The first line contains two space-separated integers, n and m, the number of elements in array a and the number of elements in array b.
# The second line contains n distinct space-separated integers describing a[i] where 0 <= i < n.
# The third line m contains distinct space-separated integers describing b[j] where 0 <= i < m.

# Constraints
# 1 <= n,m <= 10
# 1 <= a[i] <= 100
# 1 <= b[j] <= 100

# Output Format
# Print the number of integers that are considered to be between a and b.

# Sample Input
# 2 3
# 2 4
# 16 32 96

# Sample Output
# 3

# Explanation
# 2 and 4 divide evenly into 4, 8, 12 and 16.
# 4, 8 and 16 divide evenly into 16, 32, 96.
# 4, 8 and 16 are the only three numbers for which each element of a is a factor and each is a factor of all elements of b. 


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here

    # Find between values of a and b that can be divided by a
    betweenValues = []
    for _ in range(max(a), min(b)+1):
        if all([_ % i == 0 for i in a]):
            betweenValues.append(_)
    print(betweenValues)
    
    # Find between values that can divide b
    divideB = []
    for _ in betweenValues:
        if all([j % _ == 0 for j in b]):
            divideB.append(_)
        
    return len(divideB)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
