def prepare(num):
    for i in range(2, len(num)):
        if num[i] != num[i-2]:
            print('NO')
            return
    for i in range(3, len(num)):
        if num[i] != num[i-2]:
            print('NO')
            return
    
    print('YES')

t = int(input())

while t > 0:
    t -= 1
    num = input()
    prepare(num)
