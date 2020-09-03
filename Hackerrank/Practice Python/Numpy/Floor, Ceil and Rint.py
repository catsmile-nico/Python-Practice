# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem?isFullScreen=true

# Sample Input
# 1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9

# Sample Output
# [ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
# [  2.   3.   4.   5.   6.   7.   8.   9.  10.]
# [  1.   2.   3.   4.   6.   7.   8.   9.  10.]


import numpy

numpy.set_printoptions(sign=' ') #to bypass? testcase error
my_array = numpy.array(list(map(float, input().split())), float)
print( numpy.floor(my_array), numpy.ceil(my_array), numpy.rint(my_array), sep="\n" )