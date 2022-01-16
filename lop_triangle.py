from decimal import ROUND_HALF_UP, Decimal
import math
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Triangle():
    def __init__(self, A, B, C) :
        self.A = A
        self.B = B
        self.C = C
        self.AB = self.vector(self.A, self.B)
        self.AC = self.vector(self.A, self.C)
        self.BC = self.vector(self.B, self.C)

    def vector(self, E, F):
        return Point(F.x - E.x, F.y - E.y)

    def distance(self, p):
        return Decimal(math.sqrt(p.x ** 2 + p.y ** 2))

    def check(self):
        tmp = self.AB.y * (self.A.x - self.C.x) - self.AB.x * (self.A.y - self.C.y)
        if tmp == 0:
            return False
        return True
    
    def area(self):
        
        if self.check() == False:
            print('INVALID')
        else:
            tmp = self.distance(self.AB) + self.distance(self.AC) + self.distance(self.BC)
            tmp = tmp.quantize(Decimal('0.001'), ROUND_HALF_UP)
            print(tmp)
        

t = int(input())
while t > 0:
    arr = input().split()
    p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
    p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
    p3 = Point(Decimal(arr[4]), Decimal(arr[5]))
    tamgiac = Triangle(p1, p2, p3)
    tamgiac.area()
    t -= 1