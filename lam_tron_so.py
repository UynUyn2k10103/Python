def solve():
    s = input()
    if len(s) < 2:
        print(s)
        return
    i = len(s) - 1
    nho = 0
    res = ""
    while i >= 0:
        a = ord (s[i]) + nho - ord('0')
        nho = 0
        if a > 9:
            a -= 10
            nho = 1
        if i > 0:
            if a >= 5:
                nho += 1
            a = 0
        res = str(a) + res
        i -= 1

    if nho != 0:
        res = chr(ord('0') + nho) + res
    print(res)


T = int(input())
for t in range(T):
    solve()