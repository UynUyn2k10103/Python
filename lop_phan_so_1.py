class PhanSo():
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    
    def ucln(self, a, b):
        while a*b != 0:
            if a >= b:
                a %= b
            else:
                b %= a
        return a + b
    
    def rutgon(self):
        u = self.ucln(self.tu, self.mau)
        self.tu //= u
        self.mau //= u
    def printf(self):
        self.rutgon()
        print(f"{self.tu}/{self.mau}")
    
a, b = map(int, input().split())

p = PhanSo(a, b)
p.printf()