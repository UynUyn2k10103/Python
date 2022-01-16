def check(k):
    if k < 2:
        return False
    for i in range(2, k):
        if i * i > k:
            break
        if k % i == 0:
            return False
    return True


def nguyen_to_cung_nhau(a, b):
    while a * b != 0:
        if a >= b:
            a %= b
        else:
            b %= a
    if a + b == 1:
        return 1
    return 0


def solve():
    n = int (input())
    k = 0
    for i in range(1, n):
        k += nguyen_to_cung_nhau(n, i)
    if check(k):
        print("YES")
    else:
        print("NO")


T = int(input())
while T != 0:
    solve()
    T -= 1



