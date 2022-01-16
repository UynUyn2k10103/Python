
def prepare(num, dem):
    if dem > 1000:
        print('-1')
        return
        
    if num % 7 == 0:
        print(num)
        return
    string = str(num)
    num += int(string[::-1])
    
    prepare(num, dem + 1)

t = int(input())

while t > 0:
    t -= 1
    num = int(input())
    prepare(num, 0)
