# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?isFullScreen=true
# https://numpy.org/doc/stable/reference/generated/numpy.around.html
# Problem : 

# Sample Input
# 2 2
# 1 2
# 3 4

# Sample Output
# [ 1.5  3.5]
# [ 1.  1.]
# 1.11803398875

import numpy as np
np.set_printoptions(sign=' ') #to bypass? testcase error

N, M = map(int, input().split())
my_array = np.array([input().split() for _ in range(N)], int)

# np.around to bypass? testcase error
print( np.mean(my_array, axis=1), np.var(my_array, axis=0), np.around(np.std(my_array, axis=None), decimals=12), sep="\n")