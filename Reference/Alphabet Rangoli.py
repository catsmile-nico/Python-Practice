alpha = "abcdefghijklmnopqrstuvwxyz"

n = int(input())
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    print("check0: "+s)
    print("check1a: "+s[::-1])
    print("check1b: "+s[1:])
    print("check2: "+(s[::-1]+s[1:]))
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print('\n'.join(L[::-1]+L[1:]))
