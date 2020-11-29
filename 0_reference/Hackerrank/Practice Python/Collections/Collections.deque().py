# https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=true
# Problem : On an empty deque d, For Line1 no. of operations, perform commands on subsequent lines of commands and sets

# Sample Input
# 6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft

# Sample Output
# 1 2

from collections import deque

d = deque()

for _ in range(int(input())):
    line = input().split()
    if len(line) > 1:
        command, count = line
        getattr(d, command)(count)
    else:
        command = str(*line)
        getattr(d, command)()

print(*d)
