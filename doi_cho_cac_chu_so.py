def solve():
    a = list(input())
    if len(a) < 2:
        print(-1)
        return
    i = len(a) - 2
    while i >= 0 and a[i] <= a[i + 1]:
        i -= 1
    if i < 0:
        print(-1)
        return
    ans = i + 1
    for j in range(i + 1, len(a)):
        if a[i] > a[j] and a[ans] < a[j]:
            ans = j

    a[i], a[ans] = a[ans], a[i]
    if a[0] == '0':
        print(-1)
        return
    print(''.join(a))
        


T = int(input())
for i in range(T):
    solve()