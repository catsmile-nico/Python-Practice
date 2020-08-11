# https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true

# Task
# You are given a complex z. Your task is to convert it to polar coordinates.

# Input Format
# A single line containing the complex number z. Note: complex() function can be used in python to convert the input as a complex number.

# Constraints
# Given number is a valid complex number

# Output Format
# Output two lines:
# The first line should contain the value of r
# The second line should contain the value of p.

# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import phase

z = complex(input())
print(abs(z))  # anglle of x and z
print(phase(z))  # z to origin