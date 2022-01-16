def solve(s, k):
    P = []
    for i in range(ord('A'), ord('Z') + 1):
        P.append(chr(i))
    
    P.append('_')
    P.append('.')

    i = len(s) - 1
    while i >= 0:
        if s[i] == '_':
            a = 26 + k 
            a %= 28
        elif s[i] == '.':
            a = (27 + k) % 28
        else:
            a = ord(s[i]) - ord('A') + k
            a %= 28
        if a == 26:
            print('_', end = '')
        elif a== 27:
            print('.', end = '')
        else:
            print(chr(a + ord('A')), end = '')
        i -= 1
    print()
while True:
    s1 = input().split()
    k = int(s1[0])
    if k == 0:
        break
    s = s1[1]
    solve(s, k)
