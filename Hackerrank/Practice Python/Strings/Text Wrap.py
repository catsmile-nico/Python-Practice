# https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true

# Input Format
# The first line contains a string, S.
# The second line contains the width, w.

# Constraints
# 0 < len(S) < 1000
# 0 < w < len(S)

# Output Format
# Print the text wrapped paragraph.

# Sample Input 0
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4

# Sample Output 0
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ


import textwrap

def wrap(string, max_width):
    
    #returnString = ""
    #for _ in range(0, len(string), max_width):
    #    returnString += string[_:_+max_width] + "\n"
    #return returnString
    
    #return "\n".join(textwrap.wrap(string, width=max_width))

    return textwrap.fill(string, width=max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
