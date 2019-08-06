num=['零','一','二','三','四','五','六','七','八','九']
kwei=['零','十','百','千','万','十','百','千','亿']


def translate(number,length):
    if length>= 1:
        prefix = number//pow(10,length)
        postfix = number%pow(10,length)
        wei = num[prefix] + kwei[length]
        if length > 4 and len(str(postfix))< 4:
            wei += kwei[4]

        if len(str(number)) - len(str(postfix)) >=2 and postfix != 0 :
            wei += kwei[0]

        return wei,postfix
    else:
        return num[number],0


number = 9876543
wei,postfix = translate(number,len(str(number))-1)
while postfix != 0:
    wei += translate(int(postfix),len(str(postfix))-1)[0]
    postfix = translate(int(postfix),len(str(postfix))-1)[1]
    print(wei)

print('########' + wei)