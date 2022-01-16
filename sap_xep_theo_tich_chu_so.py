def mulString(a):
    mul = 1
    for i in a:
        mul *= int(i)
    return mul

def solve():
    n = int(input())
    L = []
    for i in input().split():
        L.append(i)
    newL = sorted(L, key = lambda x: (mulString(x), int(x)))
    for i in newL:
        print(i, end = ' ')
    print()

T = int(input())

while T != 0:
    solve()
    T -= 1

