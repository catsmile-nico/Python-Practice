# https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true

##    Sample Input
##    this is a string   
##
##    Sample Output
##    this-is-a-string

def split_and_join(line):
    # write your code here
    #return line.replace(" ", "-")
    return "-".join(line.split())    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
