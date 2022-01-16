# import re


# def mul(L):
#     ans = 1
#     for i in L:
#         ans *= int(i)
#     return ans

# L = [8, 2, 3, -1, 7]

# print(mul(L))


def make_car(hang_xe, dong_xe, *args, **kwargs):
    print("hang xe:", hang_xe)
    print("dong xe:", dong_xe)
    for i in kwargs:
        print(i, kwargs[i])

make_car('huyndai', 'kona', color = 'blue', bks = '29A12345')
