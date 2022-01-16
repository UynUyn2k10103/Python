
t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    l = [int(i) for i in input().split()]
    a = max(l)

    for i in range(len(l)):
        if l[i] == a:
            del l[i]
            break
    
    b = max(l)

    for i in range(len(l)):
        if l[i] == b:
            del l[i]
            break
    
    c = max(l)
    print(a + b + c)