# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true

# Task
# Compute the average of all the plants with distinct heights in greenhouse.

# Input Format
# The first line contains the integer, N, the total number of plants.
# The second line contains the N space separated heights of the plants.

# Constraints
# 0 < N <= 100

# Output Format
# Output the average height value on a single line.

# Sample Input
# 10
# 161 182 161 154 176 170 167 171 170 174

# Sample Output
# 169.375


def average(array):
    # your code goes here
    distinct = set(array)
    return sum(distinct)/(len(distinct))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)