# https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true

# Task
# When she blows out the candles, she’ll only be able to blow out the tallest ones. Your task is to find out how many candles she can successfully blow out. 

# Input Format
# The first line contains a single integer, n, denoting the number of candles on the cake.
# The second line contains n space-separated integers, where each integer i describes the height of candle i.

# Constraints
# 1 <= n <= 10**5
# 1 <= ar[i] <= 10**7

# Output Format
# Return the number of candles that can be blown out on a new line.

# Sample Input 0
# 4
# 3 2 1 3

# Sample Output 0
# 2


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    maxBlown = 0
    countBlown = 0

    for _ in range(len(ar)):
        if ar[_] > maxBlown:
            maxBlown = ar[_]
            countBlown = 1 # reset : only be able to blow out the tallest candles
        elif ar[_] == maxBlown:
            countBlown += 1
    
    return countBlown
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
