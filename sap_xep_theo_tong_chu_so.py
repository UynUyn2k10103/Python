def sumString(a):
    sum = 0
    for i in a:
        sum += int(i)
    return sum

def solve():
    n = int(input())
    L = []
    for i in input().split():
        L.append(i)
    newL = sorted(L, key = lambda x: (sumString(x), int(x)))
    for i in newL:
        print(i, end = ' ')
    print()

T = int(input())

while T != 0:
    solve()
    T -= 1

