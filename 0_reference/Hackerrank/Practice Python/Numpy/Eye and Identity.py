# https://www.hackerrank.com/challenges/np-eye-and-identity/problem?isFullScreen=true
# https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html
# Problem : Print the desired NxM array.

# Sample Input
# 3 3

# Sample Output
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]

import numpy

numpy.set_printoptions(sign=' ') #to bypass? testcase error
N, M = map(int, input().split())
print( numpy.eye(N,M) )

### printoptions Examples
# # numpy.set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, suppress=None, nanstr=None, infstr=None, formatter=None, sign=None, floatmode=None, *, legacy=None)[source]
# # float precision
# numpy.set_printoptions(precision=4)
# print( numpy.array([1.123456789]) )
# # summarise long arrays
# numpy.set_printoptions(threshold=5)
# print( numpy.arange(10) )