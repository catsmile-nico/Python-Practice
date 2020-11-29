# https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true

# Task
# Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

# Input Format
# The first line of input contains an integer, M.
# The second line contains M space-separated integers.
# The third line contains an integer, N.
# The fourth line contains N space-separated integers.

# Output Format
# Output the symmetric difference integers in ascending order, one per line.

# Sample Input
# 4
# 2 4 5 9
# 4
# 2 4 11 12

# Sample Output
# 5
# 9
# 11
# 12


# Enter your code here. Read input from STDIN. Print output to STDOUT

M = int(input())
M_list = list(map(int, input().split()))

N = int(input())
N_list = list(map(int, input().split()))

M_set = set(M_list)
N_set = set(N_list)

MN_union = list(M_set.difference(N_set).union(N_set.difference(M_set)))
MN_union.sort()

print("\n".join(str(_) for _ in MN_union))