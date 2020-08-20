# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
## Given lines of input, perform their corresponding operation:
##    insert i e: Insert integer e at position i.
##    print: Print the list.
##    remove e: Delete the first occurrence of integer e.
##    append e: Insert integer e at the end of the list.
##    sort: Sort the list.
##    pop: Pop the last element from the list.
##    reverse: Reverse the list.

# Input Format
# The first line contains an integer, n , denoting the number of commands.
# Each line i of the n subsequent lines contains one of the commands described above.

# Constraints
# The elements added to the list must be integers.

# Output Format
# For each command of type print, print the list on a new line.

# Sample Input 0
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# Sample Output 0
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]


if __name__ == '__main__':
    N = int(input())
    final = []

    for _ in range(N):
        line = input().split()
        if "insert" in line:
            final.insert(int(line[1]), int(line[2]))
        if "print" in line:
            print(final)
        if "remove" in line:
            final.remove(int(line[1]))
        if "append" in line:
            final.append(int(line[1]))
        if "sort" in line:
            final.sort()
        if "pop" in line:
            final.pop()
        if "reverse" in line:
            final.reverse()    
