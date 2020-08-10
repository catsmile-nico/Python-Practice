# https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true

# Input Format
# The first line of input contains the original string. The next line contains the substring.

# Constraints
# 1 <= len(string) <= 200
# Each character in the string is an ascii character.

# Output Format
# Output the integer number indicating the total number of occurrences of the substring in the original string. 

# Sample Input
# ABCDCDC
# CDC

# Sample Output
# 2


import re

def count_substring(string, sub_string):
    regex = re.compile("(?=("+sub_string+"))")
    return len(list(regex.findall(string)))

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
