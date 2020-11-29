# https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true
# Problem : Find is all() Line2 is positive and any() Line2 is a palindromic integer.

# Sample Input
# 5
# 12 9 61 5 14 

# Sample Output
# True

N = int(input())
nList = input().split()
print(all(int(_)>=0 for _ in nList) and any(_ == _[::-1] for _ in nList)) 