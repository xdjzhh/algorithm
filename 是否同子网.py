
'''
将给出的IPV4转化为8×4 共32位的IP格式,子网掩码位长指（若为24，前24位为1，后8位为0 共计32位），然后和IPV4求与，若两运算后的IP相等则为同子网
'''

def getIpAddress(IP):
    L= IP.split('.')
    for i in range(len(L)):
        L[i] = convert(int(L[i]))
    return  L
    pass

def convert(number):
    r = bin(number)
    r = str(r)[2:]
    if len(r) < 8:
        zeros = '0'*(8-len(r))
        r = zeros+r
    return r

def mask(length):
    L = []
    for i in range(4):
        if length >= 8:
            length = length - 8
            L.append('11111111')
        else:
            s= '1'* length
            s = s + '0'*(8-length)
            length = 0
            L.append(s)
    return L

def bind(s1,s2):
    L= []
    for i in range(4):
        for j in range(8):
            if s1[i][j] =='1' and s2[i][j] == '1':
                L.append('1')
            else:
                L.append('0')
    return ''.join(L)


if __name__ == '__main__':
    IP1,IP2,length = input().split(' ')
    IP1 = getIpAddress(IP1)
    IP2 = getIpAddress(IP2)
    mask_number = mask(int(length))
    r1 = bind(IP1,mask_number)
    r2 = bind(IP2,mask_number)
    if r1 == r2:
        print('true')
    else:
        print('false')