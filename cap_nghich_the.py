n = int (input())

array = [int(i) for i in input().split()]

i = 0
res = 0
while i < n - 1:
  j = i + 1
  while j < n:
    if array[i] > array[j]:
      res += 1
    j += 1
  i += 1
print(res)