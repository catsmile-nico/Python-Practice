# https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem?isFullScreen=true

# Sample Input
# 9
# 29
# 7
# 27

# Sample Output
# 4710194409608608369201743232  

a, b, c, d =  ( int(input()) for _ in range(4) )
print (a**b + c**d)