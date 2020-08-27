# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem?isFullScreen=true
# Reference : http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
# Problem : Given mobile numbers that may have +91, 91, or 0 written before the actual 10 digit, print in +91 XXXXX XXXXX format, by completing the function.

# Sample Input
# 3
# 07895462130
# 919875641230
# 9195969878

# Sample Output
# +91 78954 62130
# +91 91959 69878
# +91 98756 41230

def wrapper(f):
    def fun(l):
        # complete the function
        f("+91 " + _[-10:-5] + " " + _[-5:] for _ in l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


