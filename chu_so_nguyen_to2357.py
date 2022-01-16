
def check(s):
    if s[-1] == '2':
        return False
    tmp = set(s)
    if len(tmp) == 4:
        return True
    return False

def Try(ans, n):
    L = [2, 3, 5, 7]
    if len(ans) == n:
        if check(ans):
            print(ans)
        return
    
    for i in L:
        Try(ans + str(i), n)

n = int(input())
Try('', n)



