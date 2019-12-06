def toBin(n):
    s = str(bin(n)[2:])
    if len(s) < 8:
        s = '0'*(8-len(s))+s
    return s
def getsup(n):
    s = toBin(n)
    L = []
    for i in range(8):
        L.append(s[i])
    if L[0]=='1':
        for i in reversed(range(8)):
            if L[i] == '0':
                L[i] = '1'
            else:
                L[i] = '0'
        for i in reversed(range(8)):
            if L[i] == '0':
                L[i] = '1'
                break
            else:
                L[i] = '0'
    return ''.join(L)

def sum(m,n,k):
    s1 = getsup(m)
    s2 = getsup(n)
    s1 = '0b' + s1
    s2 = '0b' + s2
    num = int(s1,2) + int(s2,2)
    num = bin(num)
    s = str(num[2:])
    if len(s)>k:
        return True
    else:
        return False

def solution(L):
    count = 0
    out = 0
    for i in range(L[1],L[2]+1):
        for j in range(L[3],L[4]+1):
            if sum(i,j,L[0]):
                out += 1
            count+=1
    s = out/count
    print(f'%.6f'%(s))

if __name__ == '__main__':
    s = input()
    L = s.split(' ')
    for i in range(len(L)):
        L[i] = int(L[i])
    solution(L)