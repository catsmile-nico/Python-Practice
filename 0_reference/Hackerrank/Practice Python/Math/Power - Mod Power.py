# https://www.hackerrank.com/challenges/python-power-mod-power/problem?isFullScreen=true

# Sample Input
# 3
# 4
# 5

# Sample Output
# 81
# 1


a, b, m = ( int(input()) for _ in range(3) )

print(pow(a,b))
print(pow(a,b,m))