
num = 1000001
f = [1] * num

def sang():
    f[0] = 0
    f[1] = 0
    for i in range(2, num):
        if f[i] == 0:
            continue
        if i * i >= num: 
            break
        for j in range(i * i, num, i):
            f[j] = 0


T = int(input())
sang()
L = []
for i in range(2, num):
    if f[i] == 1:
        s = str(i)
        f[i] = 0
        if f[int (s[::-1])] == 1 and s != s[::-1]:
            L.append(i)

del f

while T > 0:
    n = int(input())
    for i in L:
        if i >= n:
            break
        if int(str(i)[::-1]) >= n:
            continue
        print(i, str(i)[::-1], end=' ')
    print()
    T -= 1
