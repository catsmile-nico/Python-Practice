# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true

# Input Format
# The first line contains X, the number of shoes.
# The second line contains the space separated list of all the shoe sizes in the shop.
# The third line contains N, the number of customers.
# The next N lines contain the space separated values of the shoe size desired by the customer and x, the price of the shoe.

# Constraints
# 0 < X < 10**3
# 0 < X <= 10**3
# 20 < x < 100
# 2 < shoe size < 20

# Output Format
# Print the amount of money earned by Raghu.

# Sample Input
# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50

# Sample Output
# 200

from collections import Counter

X = int(input()) # no of shoes
sizes = Counter(list(map(int, input().split())))
N = int(input()) # no. of customer

sales = 0

for _ in range(N):
    size, price = map(int, input().split())
    if sizes[size]:
        sales += price
        sizes[size]-=1

print(sales)