# https://www.hackerrank.com/challenges/np-arrays/problem?isFullScreen=true
# https://numpy.org/doc/stable/reference/generated/numpy.flip.html
# Problem : Print the reverse NumPy array with type float.

# Sample Input
# 1 2 3 4 -8 -10

# Sample Output
# [-10.  -8.   4.   3.   2.   1.]

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    return numpy.flip(numpy.array(arr,float))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
