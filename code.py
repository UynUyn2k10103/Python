




from datetime import date

def tinh(s):
    tmp = [int(i) for i in s.split('/')] 
    s = date(tmp[-1], tmp[-2], tmp[0])
    return s

s2 = '08/03/2010' 
s1 = '01/05/2012'
s1 = tinh(s1)
s2 = tinh(s2)
t = s1 - s2
print(t.days)