# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true

Task
You are given a string S. Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.

Input Format
A single line containing the string S and integer value k separated by a space.

Constraints
0 < k <= len(S)
The string contains only UPPERCASE characters.

Output Format
Print the combinations with their replacements of string S on separate lines.

Sample Input
HACK 2

Sample Output
AA
AC
AH
AK
CC
CH
CK
HH
HK
KK


# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

S, k = input().split()

combinationS = list(combinations_with_replacement(sorted(S),int(k)))
combinationS.sort()
print("\n".join(["".join(_) for _ in combinationS]))
