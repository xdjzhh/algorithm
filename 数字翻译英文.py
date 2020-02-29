def dps(n):
    m1 = 'one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen'.split(',')
    m2 = 'twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety'.split(',')
    if(n<20):
        return m1[n-1:n]
    if(n<100):
        return [m2[n//10-2]] + dps(n%10)
    if(n<1000):
        return [m1[n//100-1]]+['hundred']+['and']+dps(n%100)
    else:
        for w,p in enumerate(('thousand','million','billion'),1):
            if(n<1000**(w+1)):
                return dps(n//(1000**w))+[p]+dps(n%1000**w)
def question():
    n = int(input())
    return ' '.join(dps(n)) or 'zero'
while(True):
    try:
        print(question())
    except:
        break