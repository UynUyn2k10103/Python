def Eratosthens():
    f = [0] * 1000000
    f[0] = -1
    f[1] = -1
    for i in range (2, 1000000):
        if f[i] == -1:
            continue
        for j in range(i * i, 1000000, i):
            f[j] = -1
    return f

n = int (input())
f = Eratosthens()
mylist = [int(i) for i in input().split()]

for i in mylist:
    if f[i] > -1:
        f[i] += 1
for i in mylist:
    if f[i] > -1:
        print(i, " ", f[i])
        f[i] = -1



