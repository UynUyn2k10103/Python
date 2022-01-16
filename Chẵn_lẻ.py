
def solve ():
  s = input()
  sum = 0
  for i in range(len(s) - 1):
    sum += int (s[i])
    if abs(int (s[i])- int(s[i + 1])) != 2:
      print("NO")
      return
  sum += int(s[-1])
  if sum % 10 == 0:
    print ("YES")
    return
  print("NO")

T = int (input())

while T != 0:
  solve()
  T -= 1