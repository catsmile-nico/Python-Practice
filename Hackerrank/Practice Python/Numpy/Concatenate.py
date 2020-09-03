# https://www.hackerrank.com/challenges/np-concatenate/problem?isFullScreen=true
# https://numpy.org/doc/stable/reference/generated/numpy.array.html
# https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html
# https://stackoverflow.com/questions/38155039/what-is-the-difference-between-native-int-type-and-the-numpy-int-types/38156888
# https://stackoverflow.com/questions/21851985/difference-between-np-int-np-int-int-and-np-int-t-in-cython
# Problem : print concatenated array of N and M
# Sample Input
# 4 3 2
# 1 2
# 1 2 
# 1 2
# 1 2
# 3 4
# 3 4
# 3 4 

# Sample Output
# [[1 2]
#  [1 2]
#  [1 2]
#  [1 2]
#  [3 4]
#  [3 4]
#  [3 4]] 

import numpy

N, M, P = map(int,input().split())
nLines = numpy.array([input().split() for _ in range(N)], int) #dtype int because output cannot have ''
mLines = numpy.array([input().split() for _ in range(M)], int)
print( numpy.concatenate( (nLines, mLines) ) )

### Concatenate Example with axis
# a = numpy.array([[1, 2], [3, 4]])
# b = numpy.array([[5, 6]])
# c = numpy.array([[5, 6], [7, 8]])
# print( numpy.concatenate((a, b), axis=0) )
# print()
# print( numpy.concatenate((a, b.T), axis=1) )
# print()
# print( numpy.concatenate((a, c), axis=1) )
# print()
# print( numpy.concatenate((a, b), axis=None) )

