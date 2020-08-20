# https://www.hackerrank.com/challenges/python-mod-divmod/problem?isFullScreen=true

# Sample Input
# 177
# 10

# Sample Output
# 17
# 7
# (17, 7)


a, b = (int(input()) for _ in range(2))

print(a//b)
print(a%b)
print(divmod(a,b))