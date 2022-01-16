n = int(input())
L = []
i = 0
while i < n:
    s = input()
    i += 1
    if s == '':
        while s == '' and i < n:
            s = input()
            i += 1
        L.append([s, -1])
    if len(L) == 0:
        L.append([s, -1])
    L[-1][1] += 1
    


for i in L:
    print(i[0] + ':', i[1])

'''
12


Home/accommodation
What kind of housing/accommodation do you live in?
Who do you live with?
How long have you lived there?


Study
Describe your education
What is your area of specialization?
Why did you choose to study that major?
'''
