# https://www.hackerrank.com/challenges/np-sum-and-prod/problem?isFullScreen=true
# Problem : Sum along axis, 0 then print product of that sum.

# Sample Input
# 2 2
# 1 2
# 3 4

# Sample Output
# 24

import numpy as np

N, M = map(int, input().split())

my_array = np.array([input().split() for _ in range(N)], int)
my_sum = np.sum(my_array, axis=0)

print( np.prod(my_sum, axis=0) )