# https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true

# Input Format
# Only one line of input containing N, the size of the rangoli.

# Constraints
# 0 < N < 27

# Output Format
# Print the alphabet rangoli in the format explained above.

# Sample Input
# 5

# Sample Output
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------


def print_rangoli(size):
    # your code goes here

    alphabets = "abcdefghijklmnopqrstuvwxyz"
    maxLength = (size*2-1) + (size-1)*2
    #eqn for max length
        #(3*2-1) + (3-1)*2 # 5+4=9
        #(10*2-1) + (10-1)*2 #19+18=37
        
    rangoliList = []

### slicing version(shorter)
    for _ in range(size):
        rangoli = "-".join(alphabets[_:size])
        rangoliList.append((rangoli[::-1] + rangoli[1:]).center(maxLength,"-"))

    print("\n".join(rangoliList[::-1]+rangoliList[1:]))

### slicing version
    # print first half
    # for _ in range(size-1, 0, -1):
        # rangoli = "-".join(alphabets[_:size])
        # print((rangoli[::-1] + rangoli[1:]).center(maxLength,"-"))
    
    # print second half
    # for _ in range(size):
        # rangoli = "-".join(alphabets[_:size])
        # print((rangoli[::-1] + rangoli[1:]).center(maxLength,"-"))

### initial version
    # print first half
    # for _ in range(size):
        # rangoli = ""
        # for bits in range(_+1):
            # rangoli += alphabets[size - 1 - bits]
            # if bits+1 == maxLength:
                # break
            # rangoli += "-"  
        # for bits in range(_, 0, -1):
            # rangoli += alphabets[size - bits]
            # if bits == 1:
                # break
            # rangoli += "-"
        # print(rangoli.center(maxLength,"-"))
    
    # print second half    
    # for _ in range(size-1, 0, -1):
        # rangoli = ""
        # for bits in range(_):
            # rangoli += alphabets[size - 1 - bits]
            # rangoli += "-"
        # for bits in range(_-1, 0, -1):
            # rangoli += alphabets[size - bits]
            # if bits == 1:
                # break
            # rangoli += "-"

        # print(rangoli.center(maxLength,"-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)