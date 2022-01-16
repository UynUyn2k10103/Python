def check(a, b):
    while a * b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    if a + b == 1:
        return 1
    else: 
        return 0

def solve():
    s = input()
    dao = s[::-1]
    if check(int(s), int(dao)) == 1:
        print("YES")
    else:
        print("NO")

T = int(input())

while T != 0:
    solve()
    T -= 1