# https://www.hackerrank.com/challenges/np-shape-reshape/problem?isFullScreen=true
# Problem : Print the 3X3 NumPy array.

# Sample Input
# 1 2 3 4 5 6 7 8 9

# Sample Output
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

import numpy

my_array = numpy.array([input().split()], int)
print(numpy.reshape(my_array,(3,3)))