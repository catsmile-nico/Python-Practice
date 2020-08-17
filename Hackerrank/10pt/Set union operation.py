# https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true

# Input Format
# The first line contains an integer, n, the number of students who have subscribed to the English newspaper.
# The second line contains n space separated roll numbers of those students.
# The third line contains b, the number of students who have subscribed to the French newspaper.
# The fourth line contains b space separated roll numbers of those students.

# Constraints
# 0 < Total number of students in college < 1000

# Output Format
# Output the total number of students who have at least one subscription.

# Sample Input
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8

# Sample Output
# 13


# Enter your code here. Read input from STDIN. Print output to STDOUT

no_of_sub_English = int(input())
n = set(input().split())
no_of_sub_French = int(input())
b = set(input().split())

print(len(n.union(b)))