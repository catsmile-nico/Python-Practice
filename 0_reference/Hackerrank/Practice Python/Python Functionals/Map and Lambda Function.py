# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem   
# Problem : fib the input() and **3 every element of the fib list using map and lambda.
# Sample Input
# 5

# Sample Output
# [0, 1, 1, 8, 27]

cube = lambda x: pow(x, 3) # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    fibList = [0, 1]
    for _ in range(n-2):
        fibList.append(fibList[_] + fibList[_+1])
    return fibList[0:n] # 0 <= N <= 15

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))