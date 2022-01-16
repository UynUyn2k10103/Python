def solve():
  f = [0, 1]
  for i in range(2, 93):
    f.append(f[i - 2] + f[i - 1])
  return f

T = int (input())
f = solve()
while T != 0:
  ans = ""
  s = input().split()
  a = int (s[0])
  b = int (s[1])
  for i in range(a, b + 1):
      ans = ans + str(f[i]) + " "
  print(ans)
  T -= 1