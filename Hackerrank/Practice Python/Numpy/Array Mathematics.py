# https://www.hackerrank.com/challenges/np-array-mathematics/problem?isFullScreen=true

# Sample Input
# 1 4
# 1 2 3 4
# 5 6 7 8

# Sample Output
# [[ 6  8 10 12]]
# [[-4 -4 -4 -4]]
# [[ 5 12 21 32]]
# [[0 0 0 0]]
# [[1 2 3 4]]
# [[    1    64  2187 65536]] 


import numpy

N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)], int)
B = numpy.array([input().split() for _ in range(N)], int)

### cleaner print
print (A+B, A-B, A*B, A//B, A%B, A**B, sep="\n")

### original print
# print(A+B)
# print(A-B)
# print(A*B)
# print(A//B)
# print(A%B)
# print(A**B)
