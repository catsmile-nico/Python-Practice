# https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true

# Print
# Print two space-separated integers on one line: the minimum sum and the maximum sum of 4 of 5 elements.

# Input Format
# A single line of five space-separated integers.

# Constraints
# 1 <= arr[i] <= 10**9

# Output Format
# Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

# Sample Input
# 1 2 3 4 5

# Sample Output
# 10 14


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    print((sum(arr)-max(arr)),(sum(arr)-min(arr)))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
