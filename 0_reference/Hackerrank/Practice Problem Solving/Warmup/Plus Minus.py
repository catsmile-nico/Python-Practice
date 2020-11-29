# https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true
# Print ratio of positive, negative, zero

# Sample Input
# 6
# -4 3 -9 0 4 1         

# Sample Output
# 0.500000
# 0.333333
# 0.166667


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    zero = 0
    positive = 0
    negative = 0
    
    for _ in range(len(arr)):
        if arr[_] > 0:
            positive += 1
        elif arr[_] < 0:
            negative += 1
        else:
            zero += 1
        
    print(positive/len(arr))
    print(negative/len(arr))
    print(zero/len(arr))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
