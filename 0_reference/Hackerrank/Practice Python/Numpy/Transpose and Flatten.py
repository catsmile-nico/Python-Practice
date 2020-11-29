# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem?isFullScreen=true
# Problem : Print the transpose array and then print the flatten.

# Sample Input
# 2 2
# 1 2
# 3 4

# Sample Output
# [[1 3]
#  [2 4]]
# [1 2 3 4]

import numpy

N, M = map(int, input().split())
my_array = numpy.array([input().split() for _ in range(N)], int) 
print( numpy.transpose(my_array) )
print( my_array.flatten() )