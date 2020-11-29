# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=true

# Sample Input
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8

# Sample Output
# 8


en, enList, fr, frList = ( set(input().split()) for _ in range(4) )
print(len(enList.symmetric_difference(frList)))