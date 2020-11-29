# https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true

# Input Format
# The first line contains the space separated elements of list A.
# The second line contains the space separated elements of list B.
# Both lists have no duplicate integer elements.

# Constraints
# 0 < A < 30
# 0 < B < 30

# Sample Input
 # 1 2
 # 3 4

# Sample Output
 # (1, 3) (1, 4) (2, 3) (2, 4)

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

if __name__ == '__main__':
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    print(*product(A,B)) #asterisk to print value of product