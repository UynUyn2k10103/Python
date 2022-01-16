def prepare(num):
    for i in range(len(num)):
        if num[i] == '1' or num[i] == '2' or num[i] == '0':
            continue
        else: 
            print('NO')
            return
    print('YES')

t = int(input())

while t > 0:
    t -= 1
    num = input()
    prepare(num)
