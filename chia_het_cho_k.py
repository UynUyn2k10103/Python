def solve(a, k, n):
    if n - a < k:
        print("-1")
        return
    b = int(a / k)
    b = (b + 1) * k
    b -= a
    while b + a <= n:
        print(b, end = ' ')
        b += k
    print()

a, k, n = map(int, input().split())

solve(a, k, n)

