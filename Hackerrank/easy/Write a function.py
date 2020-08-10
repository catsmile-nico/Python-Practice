# https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
## Identify leap years:
##    The year can be evenly divided by 4, is a leap year, unless:
##        The year can be evenly divided by 100, it is NOT a leap year, unless:
##            The year is also evenly divisible by 400. Then it is a leap year.

## Sample Input 0
## 1990
##
## Sample Output 0
## False



def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year%4 == 0):
        leap = True
        if (year%100 == 0 and year%400 != 0):
            leap = False

    return leap

year = int(input())
