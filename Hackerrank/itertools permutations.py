# https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true

# Input Format
# A single line containing the space separated string S and the integer value K.

# Constraints
# The string contains only UPPERCASE characters.

# Output Format
# Print the permutations of the string S on separate lines.

# Sample Input
# HACK 2

# Sample Output
# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH


# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

if __name__ == '__main__':
    S, k = input().split()
    line = list(S)
    line.sort()
    print("\n".join("".join(_) for _ in permutations(line,int(k))))