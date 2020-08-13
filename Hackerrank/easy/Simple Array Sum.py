# https://www.hackerrank.com/challenges/simple-array-sum/problem?isFullScreen=true

# Input Format
# The first line contains an integer, n, denoting the size of the array.
# The second line contains n space-separated integers representing the array's elements.

# Constraints
# 0 < n, ar[i] <= 1000

# Output Format
# Print the sum of the array's elements as a single integer.

# Sample Input
# 6
# 1 2 3 4 10 11

# Sample Output
# 31



#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    # Write your code here.
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()