# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true

# Task
# Calculate the average marks of the students.

# Note:
# 1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
# 2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)

# Input Format
# The first line contains an integer N, the total number of students.
# The second line contains the names of the columns in any order.
# The next N lines contains the marks, IDs, name and class, under their respective column names.

# Constraints
# 0 < N <= 100

# Output Format
# Print the average marks of the list corrected to 2 decimal places.

# Sample Input
# TESTCASE 01
# 5
# ID         MARKS      NAME       CLASS     
# 1          97         Raymond    7         
# 2          50         Steven     4         
# 3          91         Adrian     9         
# 4          72         Stewart    5         
# 5          80         Peter      6   

# TESTCASE 02
# 5
# MARKS      CLASS      NAME       ID        
# 92         2          Calum      1         
# 82         5          Scott      2         
# 94         2          Jason      3         
# 55         8          Glenn      4         
# 82         2          Fergus     5

# Sample Output
# TESTCASE 01
# 78.00

# TESTCASE 02
# 81.00


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

N = int(input())
columns = input().split()
averageMarks = 0

for _ in range(N):
    student = namedtuple("student", columns)
    row = input().split()
    averageMarks += int(student(*row).MARKS)

print(averageMarks/N)