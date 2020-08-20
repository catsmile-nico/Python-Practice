# https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true

# Input Format
# A single line of four space-separated integers denoting the respective values of x1, v1, x2, and v2.
    # x1, v1: integers, starting position and jump distance for kangaroo 1
    # x2, v2: integers, starting position and jump distance for kangaroo 2


# Constraints
# 0 <= x1 < x2 <= 10000
# 1 <= v1,v2 <= 10000

# Output Format
# Print YES if they can land on the same location at the same time; otherwise, print NO.

# Note: The two kangaroos must land at the same location after making the same number of jumps.

# Sample Input 0
# 0 3 4 2

# Sample Output 0
# YES

# Sample Input 1
# 0 2 5 3

# Sample Output 1
# NO

# Explanation 1
# The second kangaroo has a starting location that is ahead (further to the right) of the first kangaroo's starting location (i.e. x2 > x1). 
# Because the second kangaroo moves at a faster rate (meaning v2 > v1) and is already ahead of the first kangaroo, the first kangaroo will never be able to catch up. 
# Thus, we print NO. 

# Sample Output - Formula test
# 2 5 11 2


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):

    sameLocation = "NO"
    if (v2 < v1): # check catchup possible since x1 < x2
        # formula check if start difference can mod by catchup difference
        if (x2-x1)%(v1-v2) == 0:
            sameLocation = "YES"
    return sameLocation
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
