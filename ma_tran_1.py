n = int(input())
L = []
for i in range(n):
    a = [int(j) for j in input().split()]
    L.append(a)

sum1 = 0
sum2 = 0

for i in range(n):
    for j in range(n):
        if(i == j):
            continue
        if i < j:
            sum1 += L[i][j]
        else:
            sum2 += L[i][j]

k = int(input())
if abs(sum2 - sum1) <= k :
    print('YES')
else:
    print('NO')
print(abs(sum2 - sum1))