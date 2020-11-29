# https://www.hackerrank.com/challenges/validate-a-roman-number/problem?isFullScreen=true
# https://regexr.com/3a406 
# Problem : Return True if Roman numeral

# Sample Input
# CDXXI

# Sample Output
# True

# https://www.britannica.com/topic/Roman-numeral
# Change starting {0,4} to {0,3} since we only do up to 3999
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))