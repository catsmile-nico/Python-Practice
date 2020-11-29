# https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true
# Problem : Print average of X rows of N entries
# Sample Input
# 5 3
# 89 90 78 93 80
# 90 91 85 88 86  
# 91 92 83 89 90.5

# Sample Output
# 90.0 
# 91.0 
# 82.0 
# 90.0 
# 85.5        

### submited version
N, X = map(int, input().split())
averageList = list(map(float, input().split()))

for _ in range(X-1):
    averageList = [sum(_) for _ in zip(averageList, list(map(float, input().split())))]

print( "\n".join(str(_/X) for _ in averageList) )

### numpy version
# import numpy

# N, X = map(int, input().split())
# averageList = list(map(float, input().split()))

# for _ in range(X-1):
#     averageList = [sum(_) for _ in zip(averageList, list(map(float, input().split())))]

# print( "\n".join(map(str,numpy.array(averageList)/3)) )