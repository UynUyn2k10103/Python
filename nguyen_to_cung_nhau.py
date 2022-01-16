def nguyen_to_cung_nhau(a, b):
    while a * b != 0:
        if a >= b:
            a %= b
        else:
            b %= a
    return a + b

n = int(input())
a = [int(i) for i in input().split()]

a = sorted(a)

for i in range(0, n - 1):
    for j in range (i + 1, n):
        if nguyen_to_cung_nhau(a[i], a[j]) == 1:
            print(a[i], a[j])
