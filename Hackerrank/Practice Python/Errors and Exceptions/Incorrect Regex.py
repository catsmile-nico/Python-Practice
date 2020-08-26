# https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=true
# Problem : Check if Line1 no. of regex is a valid regex.

# Sample Input
# 2
# .*\+
# .*+

# Sample Output
# True
# False
import re

for _ in range(int(input())):
    try:
        re.compile(input())
        print(True)
    except re.error:
        print(False)