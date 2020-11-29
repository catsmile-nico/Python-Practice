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


for _ in range(int(input())):
    # print( "YES" if re.search(r"^(?=(?:[7-9]))[0-9]{10}$", input()) else "NO" )
    print( "YES" if re.match(r"^[7-9][0-9]{9}$", input()) else "NO" )
