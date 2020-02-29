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

'''
class NumberToHanzi():
    def __init__(self):

        self.han_list = ["零" , "一" , "二" , "三" , "四" , "五" , "六" , "七" , "八" , "九"]
        self.unit_list = ["十" , "百" , "千"]
    #
     # 把一个四位的数字字符串变成汉字字符串
    #  num_str 需要被转换的四位的数字字符串
     # 返回四位的数字字符串被转换成汉字字符串
    #
    def four_to_hanstr(self,num_str):
        result = ""
        num_len = len(num_str)
        for i in range(num_len):
            num = int(num_str[i])
            if i != num_len - 1 and num != 0 :
                result += self.han_list[num] + self.unit_list[num_len - 2 - i]
            else :
                if num == 0 and result and result[-1]=='零':
                    continue
                else:
                    result += self.han_list[num]
        return result

    def dig2cn(self,num_str):
        str_len = len(num_str)
        if str_len > 12 :
            print('数字太大，翻译不了')
            return
        # 如果大于8位，包含单位亿
        elif str_len > 8:
            hanstr = self.four_to_hanstr(num_str[:-8]) + "亿" + \
                self.four_to_hanstr(num_str[-8: -4]) + "万" + \
                self.four_to_hanstr(num_str[-4:])
        # 如果大于4位，包含单位万
        elif str_len > 4:
            hanstr = self.four_to_hanstr(num_str[:-4]) + "万" + \
                self.four_to_hanstr(num_str[-4:])
        else:
            hanstr = self.four_to_hanstr(num_str)

        if hanstr[-1]=='零':
            hanstr = hanstr[:-1]
        return hanstr

num = '50050000'
nth = NumberToHanzi()
ans = nth.dig2cn(num)
print(ans)
————————————————
版权声明：本文为CSDN博主「vivian_ll」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/vivian_ll/article/details/95172583'''