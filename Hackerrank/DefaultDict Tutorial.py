# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true

# Constraints 
# 1 <= n <= 10000
# 1 <= m <= 100
# 1 <= length of each word in the input <= 100

# Input Format
# The first line contains integers, n and m separated by a space.
# The next n lines contains the words belonging to group A.
# The next m lines contains the words belonging to group B.

# Output Format
# Using Group B keys, output values of keys found in group A.
# The value should contain the i-indexed positions of the occurrences of the i-th word separated by spaces. 

# Sample Input
# 5 2
# a
# a
# b
# a
# b
# a
# b

# Sample Output
# 1 2 4
# 3 5


from collections import defaultdict

d = defaultdict(list)

n, m = map(int, input().split())

for _ in range (1, n+1):
    d[input()].append(_)

for _ in range (m):
    group = input()
    if group in d:
        print(" ".join([str(value) for value in d[group]]))
    else:
        print(-1)