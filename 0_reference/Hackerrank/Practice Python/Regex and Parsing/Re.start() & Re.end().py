# https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true
# https://www.afternerd.com/blog/python-enumerate/#enumerate-string
# Problem : Print start and end indice of all possible matches

# Sample Input
# aaadaa
# aa

# Sample Output
# (0, 1)  
# (1, 2)
# (4, 5)

import re

S = input()
k = input()
pattern = re.compile(k)
m = pattern.search(S)

if m == None: 
    print((-1, -1))

### final answer
else:
    indice_start = 0
    while m:
        print((m.start()+indice_start, m.end()-1+indice_start))
        indice_start = indice_start + m.start() + 1
        S = S[m.start()+1:]
        m = pattern.search(S)

### answer without start() & end(), using match to search from starting
# else:
#     for idx, ch in enumerate(S):
#         if pattern.match(S[idx:]):
#             print(idx, idx+len(k)-1)

### initial answer 
# else:
#     indice_start = 0
#     while m:
#         print((m.start()+indice_start, m.end()-1+indice_start))
#         indice_start = indice_start + m.end()-1
#         S = S[m.start()+1:]
#         m = re.search(pattern, S)




