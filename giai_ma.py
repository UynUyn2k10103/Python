def solve():
    s = input()
    res = ""
    for i in range (len(s)):
        if s[i] >= '0' and s[i] <= '9':
            for j in range(int(s[i])):
                res = res + s[i - 1]
    print(res)


T = int(input())
while T != 0:
    solve()
    T -= 1