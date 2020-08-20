# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

# Input Format
# The first line contains an integer, N, the number of students.
# The 2N subsequent lines describe each student over 2 lines.
# - The first line contains a student's name.
# - The second line contains their grade.

# Constraints
# 2 <= N <= 5
# There will always be one or more students having the second lowest grade.

# Output Format
# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

# Sample Input 0
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

# Sample Output 0
# Berry
# Harry



if __name__ == '__main__':

    rank1 = [] #from bottom
    rank2 = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        # initial input
        if not rank1 and not rank2: 
            rank1.append([name,score])
            rank2.append([name,score])
        
        # duplicate scores for rank1
        elif float(rank1[0][1]) == score:
            rank1.append([name,score])
            # incase initial input is the duplicate
            if float(rank2[0][1]) == score:
                rank2.append([name,score])

        # duplicate scores for rank2
        elif float(rank2[0][1]) == score:
            rank2.append([name,score])
        
        # if score bigger than 2
        elif float(rank2[0][1]) < score:
            # but rank2 and rank1 is initial
            if float(rank2[0][1]) == float(rank1[0][1]):
                rank2 = []
                rank2.append([name,score])
            else:
                continue

        # if score smaller        
        elif float(rank1[0][1]) > score:
            if float(rank2[0][1]) > score:
                rank2 = rank1 
            rank1 = []
            rank1.append([name,score]) 

        elif float(rank2[0][1]) > score:
            rank2 = []
            rank2.append([name,score]) 
        
    #print("rank1: "+str(rank1))
    #print("rank2: "+str(rank2))
    rank2.sort()
    for _1,_2 in rank2:
        print(_1)

