
def solve():
  n = int (input())
  s = "1"
  i = 2
  while i * i <= n:
    dem = 0
    while n % i == 0:
      dem += 1
      n /= i
    if dem != 0:
      s = s + " * " + str(i) + "^" + str(dem)
    i += 1
  if n != 1:
    s = s + " * " + str(int(n)) + "^" + str(1)
  print(s)

T = int (input())
while T != 0:
  solve()
  T -= 1
