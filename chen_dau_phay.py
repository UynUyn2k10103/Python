def solve():
    s = input()
    if len(s) <= 3:
        print(s)
        return
    if len(s) % 3 == 0:
        n = 0
    elif len(s) % 3 == 1:
        n = 1
        print(s[0]+ ',', end = '')
    else:
        n = 2
        print(s[0:2] + ',', end = '')

    for i in range(n, len(s) - 3, 3):
        print(s[i : (i + 3)] + ',', end = '')
    print(s[-3:len(s)], end = '')
solve()