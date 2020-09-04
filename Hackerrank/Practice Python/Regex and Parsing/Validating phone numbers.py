# https://www.hackerrank.com/challenges/validating-the-phone-number/problem?isFullScreen=true
# Problem : Find valid phone number

# Sample Input
# 2
# 9587456281
# 1252478965

# Sample Output
# YES
# NO


import re

# start with 7,8,9 [7-9])
# (?=(?:###)) to include the above in search, insert at ### position 
# 10 digit [0-9]{10}

for _ in range(int(input())):
    print( "Valid" if re.search(r"^(?=(?:[7-9]))[0-9]{10}$", input()) else "Invalid" )
