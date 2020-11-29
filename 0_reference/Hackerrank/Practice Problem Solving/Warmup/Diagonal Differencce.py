# https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true

# Input Format
# The first line contains a single integer, n, the number of rows and columns in the square matrix arr.
# Each of the next n lines describes a row, arr[i], and consists of n space-separated integers arr[i][j].

# Constraints
# -100 <= arr[i][j] <= 100

# Output Format
# Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

# Sample Input
# 3
# 11 2 4
# 4 5 6
# 10 8 -12

# Sample Output
# 15 # (11+5+(-12)) - (4+5+10)


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    leftToRight = 0
    for _ in range(len(arr)):
        leftToRight += arr[_][_]
    
    rightToLeft = 0
    for _ in range(len(arr)):
        rightToLeft += arr[_][(len(arr)-1) - _]

    return abs(leftToRight - rightToLeft)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
