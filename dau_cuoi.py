
def solve ():
  s = input()
  if s[0] == s[-2] and s[1] == s[-1]:
    print ("YES")
  else:
    print("NO")

T = int (input())

while T != 0:
  solve()
  T -= 1