# https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true

# Input Format
# The first line contains 2 space separated integers K and M.
# The next K lines each contains an integer N, denoting the number of elements in the i**th list, followed by N space separated integers denoting the elements in the list.

# Constraints
# 1 <= K <= 7
# 1 <= M <= 1000
# 1 <= N <= 7
# 1 <= Magnitude of elements in the list <= 10**9

# Output Format
# Output a single integer denoting the value S(max).

# Sample Input
# 3 1000
# 2 5 4
# 3 7 8 9 
# 5 5 7 8 9 10 

# Sample Output
# 206

k, m = map(int, input().split())

maxX = []

# make list of "input list"
for _ in range(k):
    maxX.append(list(map(int, input().split()))[1:]) #[1:] to remove Ni

import itertools

# make list of cartesian product
cartesian = list(itertools.product(*maxX))

# implement cartesian into equation and make list of outputlm
equationList = []

for _ in cartesian:
    sumElement = 0
    for element in _:
        sumElement += element*element
    equationList.append(sumElement%m)
    
print(max(equationList))

# get max from list

c-b-a-b-c 9
e-d-c-b-a-b-c-d-e 17
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j 37