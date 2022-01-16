n = int(input()) 
mylist = [int(i) for i in input().split()]
res = 0
for i in range(len(mylist) - 1):
    if mylist[i] != mylist[i + 1]:
        res += 1
print(res)