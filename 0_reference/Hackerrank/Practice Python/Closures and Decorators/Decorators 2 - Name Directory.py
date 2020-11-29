# https://www.hackerrank.com/challenges/decorators-2-name-directory/problem?isFullScreen=true
# https://docs.python.org/2/library/operator.html
# Given N list of names, print using name_format() in ascending order of age, by completing the function.

# Sample Input
# 3
# Mike Thomson 20 M
# Robert Bustle 32 M
# Andria Bustle 30 F

# Sample Output
# Mr. Mike Thomson
# Ms. Andria Bustle
# Mr. Robert Bustle

import operator

def person_lister(f):
    def inner(people):
        # complete the function
        # 9/12 test result answer
            # people.sort(key=operator.itemgetter(2))
            # return map(f, people)
        # 12/12 test result answer : cannot convert 3rd field to int when using itemgetter
        return map(f, sorted(people, key=lambda _ : int(_[2])))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')