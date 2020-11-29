# https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true
# Reference : https://realpython.com/python-sets/
# Problem : Check if A is strict/proper superset of n sets

# Sample Input 0
# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 100 11 12

# Sample Output 0
# False

A = set(input().split())
n = int(input())

isSuperSet = False

for _ in range(n):
    if (set(input().split()).issuperset(A)):
        isSuperSet = True
    else:
        isSuperSet = False
        break

print(isSuperSet)