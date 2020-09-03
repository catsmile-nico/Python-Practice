# https://www.hackerrank.com/challenges/np-linear-algebra/problem?isFullScreen=true
# https://numpy.org/doc/stable/reference/routines.linalg.html
# Problem : Print the determinant of array A rounded to 2 decimal place.

# Sample Input
# 2
# 1.1 1.1
# 1.1 1.1

# Sample Output
# 0.0

import numpy as np

N = int(input())
A = np.array([input().split() for _ in range(N)], float)

print( np.around(np.linalg.det(A), decimals=2) )