# https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=true
# https://www.rexegg.com/regex-quickstart.html
# Problem : Extract color codes from input

# Sample Input
# 11
# #BED
# {
#     color: #FfFdF8; background-color:#aef;
#     font-size: 123px;
#     background: -webkit-linear-gradient(top, #f9f9f9, #fff);
# }
# #Cab
# {
#     background-color: #ABC;
#     border: 2px dashed #fff;
# }   

# Sample Output
# #FfFdF8
# #aef
# #f9f9f9
# #fff
# #ABC
# #fff

import re

for _ in range(int(input())):
    m = re.findall(r"[\s:](#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})", input())
    if m: 
        print(*m, sep="\n")