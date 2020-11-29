# https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true
# Problem : Compute the min along axis 1 and then print the max of that result. 

# Sample Input
# 4 2
# 2 5
# 3 7
# 1 3
# 4 0

# Sample Output
# 3

import numpy as np

N, M = map(int, input().split())

my_array = np.array([input().split() for _ in range(N)], int)
my_min = np.min(my_array, axis=1)

print( np.max(my_min) )