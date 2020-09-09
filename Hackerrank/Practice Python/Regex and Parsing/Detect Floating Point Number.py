# https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=true
# Problem : Output True if Roman Numerals

# Sample Input 0
# 4
# 4.0O0
# -1.00
# +4.54
# SomeRandomStuff

# Sample Output 0
# False
# True
# True
# False

# [-+]?
# [\d]*
# [\d]+
regex_pattern = r"^[-+]?[\d]*\.[\d]+$"

import re
for _ in range(int(input())):
    print(str(bool(re.match(regex_pattern, input()))))