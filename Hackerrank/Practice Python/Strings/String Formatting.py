# https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true

# Input Format
# A single integer denoting n.

# Constraints
# 1 <= n <= 99

# Output Format
# Print n lines where each line i (in the range l <= i <= n) contains the respective decimal, octal, capitalized hexadecimal, and binary values of i. Each printed value must be formatted to the width of the binary value of n. 

# Sample Input
    # 2

# Sample Output 
     # 1  1  1  1
     # 2  2  2 10

def print_formatted(number):
    # your code goes here
    unformatted = []
    formatWidth = len("{0:b}".format(number))
    
    #https://docs.python.org/3/library/string.html#format-specification-mini-language
    for _ in range(1, number+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(_,width=formatWidth)
    
#---first try
    # width = len(str(bin(number))[2:])

    # for _ in range(1, number+1):
        # print(str(_).rjust(width), \
                # str(oct(_))[2:].rjust(width), \
                # str(hex(_))[2:].upper().rjust(width), \
                # str(bin(_))[2:].rjust(width))
       
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)