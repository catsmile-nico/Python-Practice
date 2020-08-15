# https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true

# Input Format
# A single integer, n, denoting the size of the staircase.

# Constraints
# 0 < n <= 100

# Output Format
# Print a staircase of size n using # symbols and spaces.

# Note: The last line must have 0 spaces in it. 

# Sample Input
# 6 

# Sample Output
     #
    ##
   ###
  ####
 #####
######


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for _ in range(1, n+1):
        print(("#"*_).rjust(n))

if __name__ == '__main__':
    n = int(input())

    staircase(n)
