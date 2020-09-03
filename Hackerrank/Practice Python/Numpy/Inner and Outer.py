# https://www.hackerrank.com/challenges/np-inner-and-outer/problem?isFullScreen=true
# Problem : First, print the inner product. Second, print the outer product.
# Sample Input
# 0 1
# 2 3

# Sample Output
# 3
# [[0 0]
#  [2 3]]


import numpy as np

A = np.array(input().split(), int)
B = np.array(input().split(), int)
print( np.inner(A,B), np.outer(A,B), sep="\n" )