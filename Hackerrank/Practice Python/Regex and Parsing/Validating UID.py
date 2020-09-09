# https://www.hackerrank.com/challenges/validating-uid/problem?isFullScreen=true
# Problem : Verify UID sequence is correct

# Sample Input
# 2
# B1CD102354
# B1CDEF2354

# Sample Output
# Invalid
# Valid

import re
 
# at least2 uppercase (.*[A-Z]){2,}
# at least 3 digit (.*[0-9]){3,}
# (?=(?:###){###}) to include the above in search, insert at ### position 
# only alphanumeric characters + exactly 10 characters [a-zA-Z0-9]{10}
# no repeat (?!.*(.).*\1) #https://stackoverflow.com/questions/12870489/regex-to-match-a-word-with-unique-non-repeating-characters

### Trial function
# def verify_UID(fv_UID):
#     return re.search(r"(.*[0-9]){3,}", fv_UID)

# for _ in range(int(input())):
#     print(verify_UID(input()))

### Final answer
for _ in range(int(input())):
    print( "Valid" if re.search(r"^(?!.*(.).*\1)(?=(?:.*[A-Z]){2,})(?=(?:.*[0-9]){3,})[a-zA-Z0-9]{10}$", input()) else "Invalid" )
    # print( "Valid" if re.match(r"^(?!.*(.).*\1)(?=(?:.*[A-Z]){2,})(?=(?:.*[0-9]){3,})[a-zA-Z0-9]{10}$", input()) else "Invalid" )

### Alternate cleaner/re-usable regex answer
# two_or_more_uppercase = r"(.*[A-Z]){2,}"
# three_or_more_digit = r"(.*[0-9]){3,}"
# only_10_alphanum = r"[a-zA-Z0-9]{10}"
# no_repeat = r"(?!.*(.).*\1)"
# regex_filter = two_or_more_uppercase, three_or_more_digit, only_10_alphanum, no_repeat

# for _ in range(int(input())):
#     uid = input()
#     print("Valid" if all([re.match(__, uid) for __ in regex_filter]) else "Invalid")