# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?isFullScreen=true
# Problem : Print the array using the numpy.zeros tool and then print the array with the numpy.ones tool. 
#           Each integer input representing the size of different dimensions

# Sample Input 0
# 3 3 3

# Sample Output 0
# [[[0 0 0]
#   [0 0 0]
#   [0 0 0]]

#  [[0 0 0]
#   [0 0 0]
#   [0 0 0]]

#  [[0 0 0]
#   [0 0 0]
#   [0 0 0]]]
# [[[1 1 1]
#   [1 1 1]
#   [1 1 1]]

#  [[1 1 1]
#   [1 1 1]
#   [1 1 1]]

#  [[1 1 1]
#   [1 1 1]
#   [1 1 1]]]


import numpy

### corrected version due to constraints 1 <= each integer <= 3
integer = list(map(int, input().split()))

print ( numpy.zeros(integer, int) )
print ( numpy.ones(integer, int) )

### initial version
# i1, i2, i3 = map(int, input().split())

# print ( numpy.zeros((i1,i2,i3), int) )
# print ( numpy.ones((i1,i2,i3), int) )

