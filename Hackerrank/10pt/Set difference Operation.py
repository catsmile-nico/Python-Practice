# https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true

# Sample Input
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8

# Sample Output
# 4


n, nList, b, bList = ( set(input().split()) for _ in range(4) )
print(len(nList.difference(bList)))