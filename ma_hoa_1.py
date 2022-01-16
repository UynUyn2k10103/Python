def solve():
    s = input()
    res = ""
    i = 0
    while i < len(s):
        dem = 0
        a = s[i]
        while i < len(s) and a == s[i]:
            dem += 1
            i += 1
        res = res + str(dem) + a

    print(res)


T = int(input())
while T != 0:
    solve()
    T -= 1