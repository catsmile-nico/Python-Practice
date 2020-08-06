import re

# using verbose mode to format adding comments and spaces
regex = re.compile(r"""
(\d\d\d-)|      # area code (without parenthesis wtih dash)
(\(\d\d\d\))    # -or- area code with parenthesis no dash
\d\d\d      # first 3 digits
-           # second dash
\d\d\d\d    #
""", re.VERBOSE | re.DOTALL | re.VERBOSE) #combine multiple args using bitwise operator

mo = regex.search("(523) 234-2341")
print(mo)
