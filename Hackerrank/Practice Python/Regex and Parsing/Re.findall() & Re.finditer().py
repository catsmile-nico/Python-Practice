# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?isFullScreen=true
# https://www.rexegg.com/regex-disambiguation.html#lookbehind
# Problem : Find substring that contain 2 or more vowel

# Sample Input
# rabcdeefgyYhFjkIoomnpOeorteeeeet

# Sample Output
# ee
# Ioo
# Oeo
# eeeee

import re

consonants = "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"

# main group ([aeiouAEIOU]{2,})
# outside ["+consonants+"], "Lookbehind After the match:"
regfind = re.findall(r"(?<=["+consonants+"])([aeiouAEIOU]{2,})["+consonants+"]", input())
print("\n".join(regfind) if regfind else -1)
