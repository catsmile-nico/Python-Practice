# https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true
# Given n, print the square of each number on a separate line.

## Sample Input 0
## 5
##
## Sample Output 0
## 0
## 1
## 4
## 9
## 16

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        print(_**2)
