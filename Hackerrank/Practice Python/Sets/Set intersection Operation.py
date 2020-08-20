# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true

# Sample Input
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8

# Sample Output
# 5


# --- Initial Answer
# n = int(input())
# nList = set(input().split())
# b = int(input())
# bList = input().split()
# print(len(nList.intersection(bList)))

# --- Improved Answer
n, nList, b, bList = ( set(input().split()) for _ in range(4) )
print(len(nList.intersection(bList)))