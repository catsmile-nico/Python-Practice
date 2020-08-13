# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true

# Task
# You are the manager of a supermarket.
# You have a list of N items together with their prices that consumers bought on a particular day.
# Your task is to print each item_name and net_price in order of its first occurrence.

# item_name = Name of the item.
# net_price = Quantity of the item sold multiplied by the price of each item.

# Input Format
# The first line contains the number of items, N.
# The next N lines contains the item's name and price, separated by a space.

# Constraints
# 0 < N <= 100

# Output Format
# Print the item_name and net_price in order of its first occurrence.

# Sample Input
# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30

# Sample Output
# BANANA FRIES 12
# POTATO CHIPS 60
# APPLE JUICE 20
# CANDY 20


# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

oDict = OrderedDict()

for _ in range(int(input())):
    N = list(input().split())
    name = " ".join(N[:-1])
    price = int(N[-1])

    if name in oDict:
        oDict[name] += price
    else:
        oDict[name] = price

for n, p in oDict.items():
    print("%s %s" % (n,p))