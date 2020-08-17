# https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true

# Input Format
# The first line contains an integer N, the total number of country stamps.
# The next N lines contains the name of the country where the stamp is from.

# Constraints
# 0 < N < 1000

# Output Format
# Output the total number of distinct country stamps on a single line.

# Sample Input
# 7
# UK
# China
# USA
# France
# New Zealand
# UK
# France 

# Sample Output
# 5


# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
print(len(set([input() for _ in range(N)])))