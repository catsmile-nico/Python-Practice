# https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true

# Input Format
# A single line containing a string S.

# Constraints
# 0 < len(S) < 1000

# Output Format
# In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if S has any alphabetical characters. Otherwise, print False.
# In the third line, print True if S has any digits. Otherwise, print False.
# In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if S has any uppercase characters. Otherwise, print False.

# Sample Input
# qA2

# Sample Output
# True
# True
# True
# True
# True


if __name__ == '__main__':
    s = input()
    
    # check if any alnum
    print(any(_.isalnum() for _ in s))
    # check if any alpha
    print(any(_.isalpha() for _ in s))
    # check if any digit
    print(any(_.isdigit() for _ in s))
    # check if any lower
    print(any(_.islower() for _ in s))
    # check if any upper
    print(any(_.isupper() for _ in s))