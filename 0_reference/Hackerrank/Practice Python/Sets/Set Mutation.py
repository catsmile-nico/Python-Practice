# https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true
# Problem : For Line1 elements in Line2, perform Line3 no. of commands on subsequent lines of commands and sets

# Sample Input
#  16
#  1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
#  4
#  intersection_update 10
#  2 3 5 6 8 9 1 4 7 11
#  update 2
#  55 66
#  symmetric_difference_update 5
#  22 7 35 62 58
#  difference_update 7
#  11 22 35 55 58 62 66

# Sample Output
# 38


### initial version
countA = int(input())
setA = set(map(int, input().split()))

for _ in range(int(input())):
    command, count = input().split()
    nextSet = set(map(int, input().split()))

    if "intersection" in command:
        setA.intersection_update(nextSet)
    elif "symmetric_difference" in command:
        setA.symmetric_difference_update(nextSet)
    elif "difference" in command:
        setA.difference_update(nextSet)
    else:
        setA.update(nextSet)
    
print(sum(setA))


### getAttr using existing input command
# countA = int(input())
# setA = set(map(int, input().split()))

# for _ in range(int(input())):
#     command, count = input().split()
#     nextSet = set(map(int, input().split()))

#     getattr(setA, command)(nextSet)

# print(sum(setA))