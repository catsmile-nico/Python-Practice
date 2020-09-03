# https://www.hackerrank.com/challenges/np-polynomials/problem?isFullScreen=true
# https://numpy.org/doc/stable/reference/generated/numpy.polyval.html#numpy.polyval
# Problem : Given coefficients of polynomial P, find value of P at point x.

# Sample Input
# 1.1 2 3
# 0

# Sample Output
# 3.0

import numpy as np

P = list(map(float, input().split()))
x = int(input())

print( np.polyval(P, x) )