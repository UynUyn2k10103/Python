def solve ():
  s = input() 
  dem = 0
  for i in s:
    if i <= 'z':
      if i >= 'a':
        dem += 1
  if dem >= len(s) - dem:
    print(s.lower())
  else:
    print(s.upper())

T = 1

while T != 0:
  solve()
  T -= 1