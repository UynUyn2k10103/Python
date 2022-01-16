
dem = 0

num = 1
while dem < 30:
    ok = 1
    num += 1
    for i in range(2, num):
        if i ** 2 > num:
            break
        if num % i == 0:
            ok = 0
            break
    if ok:
        dem += 1

print(num)  

