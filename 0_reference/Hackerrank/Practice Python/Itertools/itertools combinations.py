# https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true

# Task
# You are given a string S.
# Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

# Input Format
# A single line containing the string S and integer value k separated by a space.

# Constraints
# 0 < k <= len(S)
# The string contains only UPPERCASE characters.

# Output Format
# Print the different combinations of string S on separate lines.

# Sample Input
# HACK 2

# Sample Output
# A
# C
# H
# K
# AC
# AH
# AK
# CH
# CK
# HK


# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

S, k = input().split()

for _ in range(1, int(k)+1):
    combinationS = list(combinations(sorted(S),_))
    combinationS.sort()
    print("\n".join(["".join(_) for _ in combinationS]))

