# https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true
# Problem : Find the non-recurring number where all other numbers recur by K

# Sample Input
# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 

# Sample Output
# 8


### initial version
K = int(input())
roomList = map(int, input().split())
uniqueList = set()
filteredList = set()

for _ in roomList:
    if _ in uniqueList:
        filteredList.add(_)
    else:
        uniqueList.add(_)

print(*filteredList.symmetric_difference(uniqueList))

### math version, create set > sum of set * K - original list > remainder is Captain*(K-1)
# K = int(input())
# roomList = list(map(int, input().split()))
# print(((sum(set(roomList))*K)-(sum(roomList)))//(K-1))

### list slicing version
# K = int(input())
# roomList = list(map(int, input().split()))
# roomList.sort()
# print(*set(roomList[0::2]).symmetric_difference(set(roomList[1::2])))