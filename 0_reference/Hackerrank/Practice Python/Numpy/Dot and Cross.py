# https://www.hackerrank.com/challenges/np-dot-and-cross/problem?isFullScreen=true
# https://numpy.org/doc/stable/reference/generated/numpy.dot.html
# https://numpy.org/doc/stable/reference/generated/numpy.cross.html?highlight=cross#numpy.cross
# Problem : Given 2 array of N x N, compute their matrix product
# Sample Input
# 2
# 1 2
# 3 4
# 1 2
# 3 4

# Sample Output
# [[ 7 10]
#  [15 22]]

import numpy as np

N = int(input())

A = np.array([input().split() for _ in range(N)], int)
B = np.array([input().split() for _ in range(N)], int)

print(np.dot(A,B))