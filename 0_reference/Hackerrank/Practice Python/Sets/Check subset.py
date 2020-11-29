# https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true
# Problem : Given Line1 sets of Aset and Bset, output if Aset is subset of Bset.

# Sample Input
# 3
# 5
# 1 2 3 5 6
# 9
# 9 8 5 6 3 2 1 4 7
# 1
# 2
# 5
# 3 6 5 4 1
# 7
# 1 2 3 5 6 8 9
# 3
# 9 8 2

# Sample Output
# True 
# False
# False

### initial version
# T = int(input())

# for _ in range(T):
#     countA = input()
#     testCaseA = set(input().split())
#     countB = input()
#     testCaseB = set(input().split())

#     print(testCaseA.issubset(testCaseB))

### shorten version
for _ in range(int(input())):
    countA, testCaseA, countB, testCaseB = input(), set(input().split()), input(), set(input().split())
    print(testCaseA.issubset(testCaseB))