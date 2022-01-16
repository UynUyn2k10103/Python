def solve():
    a, b, c = map(float, input().split())
    dem = 0
    b /= 100
    while a < c:
        dem += 1
        a = (1 + b) * a
    print(dem)
T = int(input())
for t in range(T):
    solve()