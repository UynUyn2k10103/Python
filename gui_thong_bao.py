

T = int(input())

while T > 0:
    T -= 1
    s = input()
    if len(s) <= 100:
        print(s)
        continue
    tmp = s[:100]
    if s[100] != ' ':
        tmp = tmp.split()
        tmp = tmp[:-1]
        print(' '.join(tmp))

    
'''
2
Can cu Ke hoach giang day – hoc tap hoc ky 1 nam hoc 2021 – 2022 Can cu ket qua thi hoc ky 2 va hoc ky phu ky he nam hoc 2020 – 2021
Hoc vien Cong nghe Buu chinh Vien thong to chuc khai giang truc tuyen
'''