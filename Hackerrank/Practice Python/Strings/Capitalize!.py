# https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true

# Input Format
# A single line of input containing the full name, S.

# Constraints
# 0 < len(S) < 1000
# The string consists of alphanumeric characters and spaces.
# Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc. 


# Output Format
# Print the capitalized string S

# Sample Input
# chris alan

# Sample Output
# Chris Alan


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    temp = []
    for _ in s.split(" "):
        temp.append(_.capitalize())
    return " ".join(temp)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
