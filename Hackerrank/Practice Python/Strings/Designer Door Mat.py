# https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true

# Input Format
# A single line containing the space separated values of N and M.

# Constraints
# 5 < N < 101
# 15 < M < 303

# Output Format
# Output the design pattern.

# Sample Input
# 9 27

# Sample Output
# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------



size = input().split()
pattern = ".|."

for _ in range(int(size[0])//2):
    patternString = pattern * (_*2+1)
    print(patternString.center(int(size[1]),"-"))    

print("WELCOME".center(int(size[1]),"-"))

for _ in range(int(size[0])//2-1, -1, -1):
    patternString = pattern * (_*2+1)
    print(patternString.center(int(size[1]),"-"))   

# for _ in range(int(size[0])//2):
    # shapeSection = (int(size[1]) - _*2*3 - 3) // 2
    # print("-" * shapeSection, end = "")
    # print(pattern * _, end = "")
    # print(pattern, end = "")
    # print(pattern * _, end = "")
    # print("-" * shapeSection)


# centerSection = (int(size[1]) - 7)//2
# print("-" * centerSection, end = "")
# print("WELCOME", end = "")
# print("-" * centerSection)

# for _ in range(int(size[0])//2-1, -1, -1):
    # shapeSection = (int(size[1]) - _*2*3 - 3) // 2
    # print("-" * shapeSection, end = "")
    # print(pattern * _, end = "")
    # print(pattern, end = "")
    # print(pattern * _, end = "")
    # print("-" * shapeSection)