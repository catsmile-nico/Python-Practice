# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

# Input Format
# The first line contains n. The second line contains an array A[] of n integers each separated by a space.

# Constraints
# 2 <= n <= 10
# -100 <= A[i] <= 100

# Output Format
# Print the runner-up score.

# Sample Input 0
# 5
# 2 3 6 6 5

# Sample Output 0
# 5


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    n = int(input())

    rank1 = arr[0]
    rank2 = -100

    for _ in range(n):
        if rank1 < arr[_]:
            rank2 = rank1
            rank1 = arr[_]
        elif rank1 == arr[_]:
            continue    
        elif rank2 < arr[_]:
            rank2 = arr[_]
    
    print(rank2)
