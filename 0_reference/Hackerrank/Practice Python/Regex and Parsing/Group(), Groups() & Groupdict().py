# https://www.hackerrank.com/challenges/re-group-groups/problem?isFullScreen=true
# https://stackoverflow.com/questions/8880088/regular-expression-to-match-3-or-more-consecutive-sequential-characters-and-cons/8880125
# Problem : Print first occurance of a repeating character

# Sample Input
# ..12345678910111213141516171820212223

# Sample Output
# 1

import re

m = re.search(r"([a-zA-Z\d])\1", input())
print(m.group(1) if m else -1)

### findall solution
# m = re.findall(r"([a-zA-Z\d])\1", input())
# print(m[0] if m else -1)