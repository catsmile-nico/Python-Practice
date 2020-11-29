# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem?isFullScreen=true
# https://stackoverflow.com/questions/7793950/regex-to-remove-all-text-before-a-character
# Problem : Print inputs that are valid emails

# Sample Input
# 2  
# DEXTER <dexter@hotmail.com>
# VIRUS <virus!@variable.:p>

# Sample Output
# DEXTER <dexter@hotmail.com>

# A valid email address meets the following criteria:
#     It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
#       The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
#       The domain and extension contain only English alphabetical characters.
#       The extension is 1, 2, or 3 characters in length.

import re

# ^[^<]*<       skip all characters until < 
# [a-zA-Z]      find start with english alphabetical character
# (\w|\-|\.)+   find after start any alphanumeric - . _
# @             find @
# [A-Za-z]+     find alphabets only [a-zA-Z]
# .             find . 
# [a-zA-Z]{1,3} find alphabets only length 1-3 [a-zA-Z]{1,3}
# >             find > # require to pass all tests

for _ in range(int(input())):
    email = input()
    if re.match(r"^[^<]*<[a-zA-Z](\w|\-|\.)+@[A-Za-z]+\.[a-zA-Z]{1,3}>$", email):
        print( email )
