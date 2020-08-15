# https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true

# If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
# If the value of grade is less than 37, no rounding occurs as the result will still be a failing grade.

# Input Format
# The first line contains a single integer, n, the number of students.
# Each line of the subsequent lines contains a single integer, grades[i], denoting student i's grade.

# Constraints
# 1 <= n <= 60
# 0 <= grades[i] <= 100

# Output Format
# For each grades[i], print the rounded grade on a new line.

# Sample Input 0
# 4
# 73
# 67
# 38
# 33

# Sample Output 0
# 75
# 67
# 40
# 33


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here

    for _ in range(len(grades)):
        if grades[_] < 38 or grades[_]%5 == 0:
            continue
        elif (grades[_]%5) >= 3:
            grades[_] = grades[_] + (5 - grades[_]%5)

    return grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
