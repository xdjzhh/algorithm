import re
num=['零','壹','贰','叁','肆','伍','陆','柒','捌','玖']
kwei=['零','拾','佰','仟','万','拾','佰','仟','亿','拾','佰','仟','万']
point = ['元','角','分','整']


def translate(number,length):
    if length>= 1:
        prefix = number//pow(10,length)
        postfix = number%pow(10,length)
        wei = num[prefix] + kwei[length]
        flag = False
        if (not flag) and length > 12 and len(str(postfix)) < 12:
            print(wei)
            wei += kwei[12]
            flag = True
        elif (not flag) and length > 8 and len(str(postfix)) < 8:
            wei += kwei[8]
            flag = True
        elif (not flag) and length > 4 and len(str(postfix))< 4:
            wei += kwei[4]
            flag = True

        if len(str(number)) - len(str(postfix)) >=2 and postfix != 0 :
            wei += kwei[0]

        return wei,postfix
    else:
        return num[number],0


def point(number,length):
    if length == 1:
        return str(num[int(number[0])]) + '角'
    else:
        if number[0] == '0':
            return '零'+num[int(number[1])]+'分'
        else:
            return num[int(number[0])]+'角'+num[int(number[1])]+'分'

number_list = input()
input_list = re.sub('\[|\]|\"','',number_list)
input_list = list(map(float,input_list.split(',')))

input_split = []
for index in range(len(input_list)):
    input_split.append(str(input_list[index]).split('.'))

result = []
for i in input_split:
    wei,postfix = translate(int(i[0]),len(i[0])-1)
    while postfix != 0:
        wei += translate(int(postfix),len(str(postfix))-1)[0]
        postfix = translate(int(postfix),len(str(postfix))-1)[1]

    # print('########' + wei)

    if int(i[1]) == 0:
        wei += '元整'
    else:
        wei += '元'
        wei += point(i[1],len(i[1]))
    # print('完整的：' + wei)
    result.append('"'+wei+'"')

print('['+','.join(i for i in result)+']')